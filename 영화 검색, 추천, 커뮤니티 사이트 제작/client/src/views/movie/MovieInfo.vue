<template>
  <div v-if="selectedMovieDetail">

    <div class="row container">
      <div class="col-4">
        <img :src="`https://image.tmdb.org/t/p/w500${this.selectedMovieDetail.poster_path}`" class="img-fluid" alt="poster_path">  
      </div>
      <div class="col-8 text-start mt-5">
        <p class="fs-1">
          <span class="lobstar-title">Title: </span>
          <span>{{ selectedMovieDetail.title }}</span>
        </p>
        <hr>

        <p class="fs-5 ">
          
          <label for="rating" class="fs-5">Select Your Rate</label>
            <select class="form-select" aria-label="Default select example" v-model="rating" aria-placeholder="Select your Rate" >
              <option value="0">--기존 평점 삭제--</option>
              <option value="1">One</option>
              <option value="2">Two</option>
              <option value="3">Three</option>
              <option value="4">Four</option>
              <option value="5">Five</option>
            </select>
          <button @click="onClick" class="btn btn-outline-secondary">작성</button>
        </p>
        <div v-if="selectedRating == 0">
          평점: 평점을 등록해보세요
        </div>
        <div v-if="selectedRating == -1">
          평점: 로그인을 해주세요
        </div>
        <div v-if="selectedRating == 1">
          평점: <i class="fas fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i>
        </div>
        <div v-if="selectedRating == 2">
          평점: <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i>
        </div>
        <div v-if="selectedRating == 3">
          평점: <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i>
        </div>
        <div v-if="selectedRating == 4">
          평점: <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="far fa-star"></i>
        </div>
        <div v-if="selectedRating == 5">
          평점: <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
        </div>
        <p>
          vote_average: {{ selectedMovieDetail.vote_average }}
        </p>
        
        <p>
          release_date: {{ selectedMovieDetail.release_date }}
        </p>
        <p>
          vote_count: {{ selectedMovieDetail.vote_count }}
        </p>
        <p class="d-inline">
          Genre:
        </p>
        <p class="d-inline" v-for="genre in selectedMovieDetail.genres" :key="genre.id">
          |{{ genre.name }}|
        </p>
        <hr>
        <div>
          <p class="fs-3 overview">overview</p>
          <p>{{ selectedMovieDetail.overview }}</p>
        </div>
        <hr>
      </div>
    </div>
    
    <!-- 유튜브 영상 표시하기 -->
    <div v-if='videoURI' class="container">
      <div class="video-container col-9 ms-4">
        <iframe id="ytplayer" :src="videoURI" type="text/html"> </iframe>
      </div>
    </div>

  </div>
</template>

<script>

import { mapState } from 'vuex'


export default {
  name: 'MovieInfo',
  data: function () {
    return {
      rating: 0,
    }
  },
  components: {
    
  },
  computed: {
    ...mapState(['selectedMovieDetail', 'rated_movie_lst', 'selectedRating', 'youtube']),

    videoURI: function () {
      if (this.youtube) {
        const videoId = this.youtube['id']['videoId']
        return `https://www.youtube.com/embed/${videoId}`
      }
      else {
        return null
      }
    },
  },

  methods: {
    // 평점 클릭하는 method
    onClick: function () {
      const data = {
        movie: this.selectedMovieDetail.id,
        rating: this.rating
      }
      this.$store.dispatch('ratingMovie', data)
      this.rating = 0
    },
  
    
  },
  
}
</script>

<style>
  .offcanvas {
    color: #262223;
    background-color: #DDC6B6;
  }

  #ratingBtn {
    color: #262223;
    background-color: #DDC6B6;
  }

  .offcanvas{
    margin: 300px 100px;
  }

  /* 유튜브 관련 스타일 적용 */
  .video-container {
    position: relative;   /* iframe을 container를 기준으로 위치를 지정 */
    padding-top: 56.25%;  /*유튜브 비디오 비율을 맞추기 위한 높이 설정 */
    border-color: #DDC6B6;
  }

  .video-container > iframe {
  position: absolute;   /* container를 기준으로 위치를 지정*/
  top: 0px;
  left: 10em;
  width: 80%;
  height: 80%;
  border-radius: 15px;
  }

  i {
    color: #FFD662;
  }

  .lobstar-title {
    font-family: "Lobster Two";
  }
  .overview {
    font-family: "Lobster Two";
  }

</style>
