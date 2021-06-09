<template>

  <div>
    <div class="d-flex justify-content-center">
      <img src="@/assets/recommend.png" alt="" id="recommend_img">
    </div>

    <div class="input-group mb-3">
      <input v-model="movieTitle" type="text" id="searchBarRecommend" list="dataList" class="form-control" placeholder="영화 검색" aria-describedby="button-addon2">
      <!-- Search Bar 함수 추가 -->
      <button @click="onRecommend" class="btn btn-outline-secondary" type="button" id="button-addon2">Select</button>
        <datalist id="dataList">
          <option v-for="movie of movie_list" :key="movie.id" :value="movie.title" ></option>
        </datalist>
    </div>
    
    <div class="container">

      <div v-if="selectedMovieRecommend" class="row" id="upper-row">
          <div v-for="movie of selectedMovieRecommend.slice(0,3)" :key="movie.id" class="col-4">
            <div id='hover-card'>
              <div id='top-img' class="card bg-dark text-white " >
                <div>
                  <img class="card-img" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="Card image" width="10px" height="500rem" style="filter: brightness(50%);">
                  <div class="card-img-overlay">
                    <h5 class="card-title">{{ movie.title }}</h5>
                    <p class="card-text">Average Rate: {{ movie.vote_average }}</p>
                    <p class="card-text">{{ movie.overview }}</p>
                  </div>
                </div>
                <div class="card-footer">
                  <button @click="onRecommendClick(movie)" id="MovieInfoBtn" type="button" class="btn recommned-btn" data-bs-toggle="modal" data-bs-target="#movieInfoModal">
                    Detail
                  </button>
                </div>
              </div>
                <div id='bottom-img'>
                  <img class="card-img" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="Card image" width="10px" height="500rem">
                </div>

          </div>
        </div>
      </div>

      <div v-if="selectedMovieRecommend" class="row">
        <div v-for="movie of selectedMovieRecommend.slice(3,6)" :key="movie.id" class="col-4">
            <div id='hover-card'>
              <div id='top-img' class="card bg-dark text-white " >
                <div>
                  <img class="card-img" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="Card image" width="10px" height="500rem" style="filter: brightness(50%);">
                  <div class="card-img-overlay">
                    <h5 class="card-title">{{ movie.title }}</h5>
                    <p class="card-text">Average Rate: {{ movie.vote_average }}</p>
                    <p class="card-text">{{ movie.overview }}</p>
                  </div>
                </div>
                <div class="card-footer">
                  <button @click="onRecommendClick(movie)" id="MovieInfoBtn" type="button" class="btn recommned-btn" data-bs-toggle="modal" data-bs-target="#movieInfoModal">
                    Detail
                  </button>
                </div>
              </div>
                <div id='bottom-img'>
                  <img class="card-img" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="Card image" width="10px" height="500rem">
                </div>

          </div>
        </div>
      </div>

      <div v-else>
        <div class="container text-center">
          <div class="row">
            <div class="col fs-2">
              <hr>
              이 페이지는 영화 추천 페이지 입니다.
              <hr>
            </div>
          </div>
          <div class="row">
            <div class="col fs-5">
              평소에 재미있게 봤던 영화나 좋아하는 영화를 고르시면 <br>
              사용자들의 평점을 통해 분석하여 선택한 영화와 비슷한 영화를 추천해 드립니다. <br>
              영화를 선택해 주세요!
            </div>
          </div>

        </div>
      </div>

    </div>

  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Recommendation',
  data: function () {
    return {
      movieTitle: null,
    }
  },
  computed: {
    ...mapState(['movie_list', 'selectedMovieRecommend']),
  },
  methods: {
    onRecommend: function () {
      if (this.movieTitle === null) {
        alert('영화 제목이 올바르지 않습니다!\n영화 제목을 확인한 후 제대로 입력해 주세요!!')
      }
      else {this.$store.dispatch('selectRecommendMovie', this.movieTitle)}
      this.movieTitle = null
    },
    onRecommendClick: function (movie) {
      this.$store.dispatch('selectMovie', movie)
    }
  },
  created: function () {
    this.$store.commit('DELETE_RECOMMEND_MOVIE')
  }
}
</script>

<style>
  #hover-card {
    position: relative;
    
  }

  #top-img{
    /* filter: brightness(50%); */
    position: absolute;
    text-overflow: ellipsis;
    overflow: hidden;
  }
  #bottom-img {
    transition: .5s;
    position: absolute;
  }
  #hover-card:hover > #bottom-img {
    transform: translate(0%, 100%);
  }
  #upper-row {
    margin-bottom: 32em;
  }

  #recommend_img{
    width: 500px;
    height: 150px;
  }

  .recommned-btn{
    font-family: 'Lobster Two';
    background-color: #DDC6B6;
    color: #262223;
  }


</style>