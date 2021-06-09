<template>
  <div class="card col-4 m-3" data-bs-backdrop="true" style="width: 18rem; height: 38rem;">
    <img :src="`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`" class="card-img-top" alt="#" width="150rem" height="400em">
    <div class="card-body">
      <h5 class="card-title lobstar-title" >{{ movie.title }}</h5>
      <p class="card-text">Movie Average Rate: {{ movie.vote_average }}</p>
    </div>

    <div class="card-footer">
      <button @click="onMovieInfo" id="MovieInfoBtn" type="button" class="btn" data-bs-toggle="modal" data-bs-target="#movieInfoModal">
        Detail
      </button>
    </div>

  </div>
  
</template>

<script>
// import MovieInfo from '@/views/movie/MovieInfo.vue'
import { mapState } from 'vuex'

export default {
  name: 'MovieItem',
  data: function () {
    return {
      // movieId: `movieId${this.movie.id}`,
    }
  },
  components: {
    // MovieInfo
  },
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  computed: {
    ...mapState(['isSearch'])
  },
  methods: {
    onMovieInfo: function () {
      this.$store.dispatch('selectMovie', this.movie)
    }
  },
  // Search Bar 함수 추가
  watch: {
    isSearch: function () {
      const button = document.querySelector('#MovieInfoBtn')
      if (this.isSearch === true){
        button.click()
        this.isSearch = false
      }
    }
  }
}
</script>

<style>
.card {
  /* font-family: "Architects Daughter", "Noto Sans KR" */
  background-color: #DDC6B6;
  color: #262223;
  text-align: center;
}

.btn {
  background-color:#262223;
  color: #DDC6B6;
}

.modal-body {
  background-color: #262223;
  color: #DDC6B6;
}

.modal-footer {
  background-color: #DDC6B6;
}

.modal-header {
  background-color: #DDC6B6;
}

.card-footer {
    position: absolute;
    bottom: 0;
    width: 92%;
    padding-left: 1%;
}
</style>