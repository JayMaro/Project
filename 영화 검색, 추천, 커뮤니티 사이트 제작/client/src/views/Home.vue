<template>
  <div class="home">
    <div class="d-flex justify-content-center" id="now-playing">
      Now Playing
    </div>
    <!-- Carousel 시작 -->
    <!---->
    <vue-glide :autoplay="2000" v-model="active" v-if="now_playing_movie_list.length > 5">
      
      <vue-glide-slide v-for="movie of now_playing_movie_list" :key="movie.id">
        <div>
          <Carousel :movie="movie"/>
        </div>
      </vue-glide-slide>
    </vue-glide>

    <div class="swiper-button-down">
      <div>더 많은 영화보기</div>
      <i id="arrow-down" @click="onMovieDetail" class="fas fa-chevron-down fa-3x"></i>
    </div>

    <div class="d-flex justify-content-between m-2">
    </div>

    <div class="swiper-button-prev" @click="onRecommendation">
      <div class="swiper-icon" >
        <i class="fas fa-grip-lines"></i>
        추천 페이지
      </div>
    </div>
    <div class="swiper-button-next" @click="onBoard">
      <div class="swiper-icon" >
        자유 게시판
        <i class="fas fa-grip-lines"></i>
      </div>
    </div>

  </div>
  
</template>

<script>
// @ is an alias to /src
import { mapState } from 'vuex'
import Carousel from '@/components/Carousel.vue'

// import { Glide, GlideSlide } from 'vue-glide-js'

export default {
  name: 'Home',
  components: {
    Carousel,
    // [Glide.name]: Glide,
    // [GlideSlide.name]: GlideSlide
  },

  data: function() {
    return {
      URL_HEAD : 'https://image.tmdb.org/t/p/w500/',
      searchMovie: '',
      active: 0 ,
    }
  },

  computed: {
    ...mapState(['movie_list', 'selectedMovieDetail', 'isLogin', 'now_playing_movie_list'])

  },
  methods: {
    onMovieDetail: function(){
      this.$router.push({name: 'Movie'})
    },
    onBoard: function() {
      if (this.isLogin) {
        this.$router.push({name: 'FreeBoard'})
      }
      else {
        alert('로그인이 필요한 페이지 입니다.')
        this.$router.push({name : 'Login'})
      }
    },
    onRecommendation: function () {
      if (this.isLogin) {
        this.$router.push({name: 'Recommendation'})
      }
      else {
        alert('로그인이 필요한 페이지 입니다.')
        this.$router.push({name : 'Login'})
      }
    },
  },
  
  created: function (){
    // const kakao_code = location.search.split('=')[1]
    // if (kakao_code) {
    //   this.$store.dispatch('kakaoToken', kakao_code)
    // }
  }
}

</script>




<style>
body {
  background-color: #262223;
}

/* width: 27px; */
/* margin-top: -22px; */

.swiper-button-prev, .swiper-button-next {
  /* background-color: aquamarine; */
  position: absolute;
  top: 0%;
  height: 100%;
  z-index: 1;
  cursor: pointer;
  background-position: center;
  background-repeat: no-repeat;
  padding-right: 20px;
  padding-left: 20px;
}
/* 
.swiper-button-prev {
  left: 10px;
} */

.swiper-button-next {
  right: 0;
}

.swiper-button-prev:hover {
  background-size: 100% 100%;
  transition: .5s;
  /* transform: translate(90%); */
  background-color: white;
  color: black;
  opacity: 80%;
}

/* #3b3738 */

.swiper-button-next:hover {
  transition: .5s;
  background-color: white;
  color: black;
  opacity: 80%;
}

.swiper-icon {
  font-size: 20px;
  margin-top: 40em;
}

.swiper-button-down{
  text-align: center;
}

#arrow-down {
  cursor: pointer;;
}

.input-group{
  padding: 10px 50px;
}

#now-playing {
  font-family: 'Lobster Two';
  font-size: 40px;
}

</style>
