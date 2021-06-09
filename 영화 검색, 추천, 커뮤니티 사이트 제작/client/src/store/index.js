import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // server_url을 변수로 저장했습니다.
    server_url: 'http://127.0.0.1:8000/',
    movie_list: [],
    now_playing_movie_list: [],
    review_list: [],
    rated_movie_lst: [],
    selectGenre: 1,
    
    
    //comment_list 추가
    comment_list: [],
    selectedMovieDetail: null,
    selectedMovieRecommend: '',
    selectedRating: 0,

    //Youtube 영상 저장?
    youtube : '',

    // 지금 username 저장하기
    now_user : '',
    
    jwtHeader: '',
    isLogin: false

  },
  mutations: {
    CHANGE_ISLOGIN: function(state) {
      const check_jwt = localStorage.getItem('jwt')
      if (check_jwt) {
        state.isLogin = true
      }
      else {
        state.isLogin = false
      }
    },

    GET_MOVIE: function(state, res) {
      state.movie_list = res.data
    },

    GET_NOW_PLAYING_MOVIE: function(state, res) {
      state.now_playing_movie_list = res.data
    },

    GET_REVIEWS: function(state, res) {
      state.review_list = res.data
    },
    
    CREATE_REVIEW: function(state, res) {
      state.review_list.push(res)
    },

    // GET_RECOMMENDATION: function (state, res) {
    //   state.recommend_lst.push(res.data)
    // },

    SELECT_MOVIE: function (state, res) {
      state.selectedMovieDetail = res
      
    },
    
    GET_COMMENTS: function(state, res) {
      state.comment_list = res.data
    },

    RECOMMEND_MOVIE: function (state, res) {
      let reco_lst = []
      for (const movieId of res.data) {
        for (const movie of state.movie_list) {
          if (movieId === movie.id) {
            reco_lst.push(movie)
          }
        }
      }
      state.selectedMovieRecommend = reco_lst
    },

    DELETE_SELECT_DETAIL: function (state) {
      state.selectedMovieDetail = null
    },

    DELETE_RECOMMEND_MOVIE: function (state) {
      state.selectedMovieRecommend = ''
    },

    GET_YOUTUBE: function(state, res) {
      state.youtube = res
    },

    // 지금 username 저장하기
    SAVE_USER: function(state) {
      state.now_user = localStorage.getItem('user_name')
    },
    
    CHANGE_SELECT: function(state, res) {
      state.selectGenre = res
    }

  },
  
  actions: {
    // actions에서 무조건 기본인자로 context 적어주기, 사용 안해도 된다.
    // django에 signup view 가 실행되도록 합니다.
    signup: function (context, credentials) {
      axios({
        method: 'post',
        url: this.state.server_url + 'accounts/signup/',
        data: credentials,
      })
      .then(() => {
        router.push({ name: 'Login' })
      })
      .catch(err => {
        alert('ID와 PASSWORD를 확인해 주세요')
        console.log(err)
      })
    },

    // django의 api-token-auth 가 실행되도록 함으로써 jwt 토큰을 가지고 로그인이 됩니다.
    // login 성공시, Home 화면으로 이동합니다.
    login: function (context, credentials) {
      axios({
        method: 'post',
        url: this.state.server_url + 'accounts/api-token-auth/',
        data: credentials,
      })
      .then(res => {
        localStorage.setItem('user_name', res.config.data.split(/[:|,]/)[1])
        context.commit('SAVE_USER')

        localStorage.setItem('jwt', res.data.token)
        context.dispatch('setToken')

        context.dispatch('getRatedMovies')
        if (context.state.selectGenre !== 1) {
          context.state.selectGenre = 1
        }
        context.dispatch('getReviews')
        context.commit('CHANGE_ISLOGIN')
        router.push({ name: 'Home'})
      })
      .catch(err => {
        alert('ID와 PASSWORD를 확인해 주세요')
        console.log(err)
      })
    },

    kakaoToken: function(context, kakao_code) {
      console.log('axios 요청 보내기 전', kakao_code)
      axios({
        method: 'post',
        url: 'https://kauth.kakao.com/oauth/token',
        params: {
          grant_type : 'authorization_code',
          client_id : '0ba410c0f796197638aeaf933efde905',
          redirect_uri : 'http://localhost:8080/',
          code: kakao_code
        },
        headers: {
          'Content-type' : 'application/x-www-form-urlencoded;charset=utf-8',
          'Authorization' : '2a1cc18718a524a24be72d1663639061'
        }
      })
      .then(res => {
        console.log(res.data)
        localStorage.setItem('jwt', res.data.access_token)
        context.dispatch('setToken')

        context.commit('CHANGE_ISLOGIN')
        router.push({ name: 'Home'})
      })
      .catch(err => {
        console.log(err)
      })
    },

    // logout은 loacalStorage에 있는 jwt 토큰을 삭제하면서 Home 화면으로 이동합니다.
    logout: function (context) {
      localStorage.removeItem('jwt')
      localStorage.removeItem('user_name')
      context.dispatch('setToken')

      context.commit('CHANGE_ISLOGIN')
      context.state.rated_movie_lst = []
      if (context.state.selectGenre !== 1) {
        context.state.selectGenre = 1
      }
      router.push({ name: 'Home' })
    },

    getadminPage: function (context) {
      context.dispatch('setToken')
      axios({
        method: 'get',
        url: context.state.server_url + 'accounts/manager/',
        headers: context.state.jwtHeader
      })
      .then( res => {
        console.log(res)
        if (res.status === 200) {
          location.href = context.state.server_url+'admin/'
        }
      })
      .catch( err => {
        console.log(err)
        alert('허가되지 않은 사용자 입니다.')
        
      })
    },

    getMovie: function (context) {
      axios({
        method: 'get',
        url: this.state.server_url + 'movies/print_movie/',
      })
      .then(res => {
        context.commit('GET_MOVIE', res)
      })
      .catch(err => {
        console.log(err)
      })
    },

    getNowPlayingMovie: function (context) {
      axios({
        method: 'get',
        url: this.state.server_url + 'movies/print_now_playing_movie/',
      })
      .then(res => {
        context.commit('GET_NOW_PLAYING_MOVIE', res)
      })
      .catch(err => {
        console.log(err)
      })
    },

    createReview: function(context, review) {
      context.dispatch('setToken')
      axios({
        method: 'post',
        url: this.state.server_url + 'freeboard/',
        data: review,
        headers: context.state.jwtHeader
        })
        .then(res => {
          console.log(res)
          context.dispatch('getReviews')
          router.push({ name: 'FreeBoard' })
        })
        .catch(err => {
          console.log(err)
        })
      },
    
    getReviews: function(context) {
      if (localStorage.getItem('jwt') === null) {
        return
      }
      context.dispatch('setToken')
      axios({
        method: 'get',
        url: this.state.server_url + 'freeboard/',
        headers: context.state.jwtHeader
      })
      .then(res => {
        console.log(res)
        context.commit('GET_REVIEWS', res)
        // this.state.review_list = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },

    updateReview: function(context, arr) {
      context.dispatch('setToken')
      const [review_id, new_review]= arr
      // console.log(arr)
      axios({
        method: 'put',
        url: this.state.server_url + `freeboard/${review_id}/`,
        data: new_review,
        headers: context.state.jwtHeader
      })
      .then(res => {
        console.log(res)
        context.dispatch('getReviews')
        router.push({ name: 'FreeBoard' })
      })
      .catch(err => {
        console.log(err)
      })
    },

    createComment: function(context, arr) {
      context.dispatch('setToken')
      const [review_id, new_comment] = arr
      axios({
        method: 'post',
        url: this.state.server_url + `freeboard/${review_id}/comment/`,
        data: {content: new_comment},
        headers: context.state.jwtHeader
      })
      .then(res => {
        console.log(res)
        context.dispatch('getComments', review_id)
      })
      .catch(err => {
        console.log(err)
        alert('댓글을 입력해주세요!')
      })
    },
    
    getComments: function(context, review_id) {
      context.dispatch('setToken')
      axios({
        method: 'get',
        url: this.state.server_url + `freeboard/${review_id}/comment/`,
        headers: context.state.jwtHeader
      })
      .then(res => {
        context.commit('GET_COMMENTS', res)
      })
      .catch(err => {
        console.log(err)
      })
    },

    selectMovie: async function (context, res) {
       context.commit('SELECT_MOVIE', res)
       await context.dispatch('onYoutube', context.state.selectedMovieDetail.title)
       await context.dispatch('getMyRate')
    },

    ratingMovie: function (context, ratingData) {
      
      context.dispatch('setToken')
      axios({
        method: 'post',
        url: this.state.server_url + 'accounts/like-movie/',
        data: ratingData,
        headers: {'X-Requested-With': 'XMLHttpRequest',
          ...context.state.jwtHeader }
        })
      .then( res => {
        console.log(res.data)
        // actions 내에서 actions를 실행하고 싶을 땐 이렇게!
        context.dispatch('getRatedMovies')
        
      })
      .catch( err => {
        alert('로그인을 해주세요!')
        console.log(err)
        
      })
    },
    
    getRatedMovies: function (context) {
      if (localStorage.getItem('jwt') === null) {
        return
      }
      context.dispatch('setToken')
      axios({
        method: 'get',
        url: this.state.server_url + 'accounts/like-movie/',
        headers: {'X-Requested-With': 'XMLHttpRequest', 
          ...context.state.jwtHeader
        },
      })
      .then( res => {
        context.state.rated_movie_lst = res.data  
        if (context.state.selectedMovieDetail !== null) {
          context.dispatch('getMyRate')
        }
      })
      .catch( err => {
        console.log(err);
      })
    },

    getMyRate: function (context) {
      if (localStorage.getItem('jwt') === null) {
        context.state.selectedRating = -1
        return
      }
      for (const movie of context.state.rated_movie_lst) {
        if ( context.state.selectedMovieDetail.id === movie.movie) {
          context.state.selectedRating = movie.rating
          return
        }
      }
      context.state.selectedRating = 0
    },

    getRecommendation: function (context, id) {
      axios({
        method: 'get',
        url: this.state.server_url + 'accounts/cf' + `/${id}`,
      })
      .then( res => {
        console.log(res)
        context.commit('RECOMMEND_MOVIE', res)
      })
      .catch( err => {
        console.log(err)
      })
    },

    selectRecommendMovie: function (context, res) {
      let selectMovieId
      for (const movie of context.state.movie_list) {
        if (movie.title === res) {
          selectMovieId = movie.id
          console.log(selectMovieId);
        }
      }
      context.dispatch('getRecommendation', selectMovieId)
      

    },

    onYoutube: function(context, movie_title) {
      const query = movie_title + ' trailer'
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: query,
      }

      axios({
        url: API_URL,
        method: 'GET',
        params,
      })
      .then( res => {
        console.log(res.data.items[0])
        context.commit('GET_YOUTUBE', res.data.items[0])   // 맨 첫번째 영상 하나만 받아오기
      })
      .catch( err => {
        console.log(err)
      })

    },

    setToken: function(context) {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      context.state.jwtHeader = config
    },
    
    searchMovie: async function (context, res) {
      for (const movie of context.state.movie_list) {
        if (movie.title === res) {
          await context.dispatch('selectMovie', movie)
        }
      }
    },

    // 여기가 acthions!
  },
  
  
    getters: {
      selectedMovieList: function (state) {
        let genreMovieList = []
        if (Number(state.selectGenre) === 1) {
          genreMovieList = state.movie_list
        }
        else if (Number(state.selectGenre) === -6) {
          for (const movie of state.movie_list) {
            for (const rated_movie of state.rated_movie_lst){
              if (movie.id === rated_movie.movie) {
                genreMovieList.push(movie)
                continue
              }
            }
          }
        }
        else if (Number(state.selectGenre) === -5) {
          for (const movie of state.movie_list) {
            for (const rated_movie of state.rated_movie_lst){
              if (movie.id === rated_movie.movie && rated_movie.rating === 5) {
                genreMovieList.push(movie)
                continue
              }
            }
          }
        }
        else if (Number(state.selectGenre) === -4) {
          for (const movie of state.movie_list) {
            for (const rated_movie of state.rated_movie_lst){
              if (movie.id === rated_movie.movie && rated_movie.rating === 4) {
                genreMovieList.push(movie)
                continue
              }
            }
          }
        }
        else if (Number(state.selectGenre) === -3) {
          for (const movie of state.movie_list) {
            for (const rated_movie of state.rated_movie_lst){
              if (movie.id === rated_movie.movie && rated_movie.rating === 3) {
                genreMovieList.push(movie)
                continue
              }
            }
          }
        }
        else if (Number(state.selectGenre) === -2) {
          for (const movie of state.movie_list) {
            for (const rated_movie of state.rated_movie_lst){
              if (movie.id === rated_movie.movie && rated_movie.rating === 2) {
                genreMovieList.push(movie)
                continue
              }
            }
          }
        }
        else if (Number(state.selectGenre) === -1) {
          for (const movie of state.movie_list) {
            for (const rated_movie of state.rated_movie_lst){
              if (movie.id === rated_movie.movie && rated_movie.rating === 1) {
                genreMovieList.push(movie)
                continue
              }
            }
          }
        }
        else if (Number(state.selectGenre) === -7) {
          for (const movie of state.movie_list) {
            if (movie.now_playing === true) {
              genreMovieList.push(movie)
              continue
            }
          }
        }
        else {  
          for (const movie of state.movie_list) {
            for (const genre of movie.genres) {
              if (Number(state.selectGenre) === genre.idx){
                genreMovieList.push(movie)
                continue
              }
            }
          }
        }
        return genreMovieList
      },

      

    },

    
  modules: {
  }
})
