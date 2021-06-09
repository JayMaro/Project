<template>
  <div class="container">
    
    <label for="selectedGenre" class="fs-5">Select Your Genre</label>
      <select @change="changeSelect" class="form-select" aria-label="Default select example" v-model="selectedGenre" aria-placeholder="Select your Rate" id="selectedGenre">
        <option value=1>ALL</option>
        <option value=-7>Now Playing</option>
        <option value=-1>MyRatedMovie - 1</option>
        <option value=-2>MyRatedMovie - 2</option>
        <option value=-3>MyRatedMovie - 3</option>
        <option value=-4>MyRatedMovie - 4</option>
        <option value=-5>MyRatedMovie - 5</option>
        <option value=-6>MyRatedMovie - ALL</option>
        <option value=28 >Action</option>
        <option value=12>Adventure</option>
        <option value=16>Animation</option>
        <option value=35>Comedy</option>
        <option value=80>Crime</option>
        <option value=99>Documentary</option>
        <option value=18>Drama</option>
        <option value=10751>Family</option>
        <option value=14>Fantasy</option>
        <option value=36>History</option>
        <option value=27>Horror</option>
        <option value=10402>Music</option>
        <option value=9648>Mystery</option>
        <option value=10749>Romance</option>
        <option value=878>Science Fiction</option>
        <option value=10770>TV Movie</option>
        <option value=53>Thriller</option>
        <option value=10752>War</option>
        <option value=37>Western</option>
      </select>

    <div class="row" v-if="selectedMovieList.length > 0">
      <MovieItem v-for="movie in selectedMovieList" :key="movie.id" :movie="movie" />
    </div>
    <div v-else class='d-flex justify-content-center mt-5' >
      
      <h2><hr>
        영화 목록이 존재하지 않습니다.
        <hr></h2>
      
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import MovieItem from '@/views/movie/MovieItem.vue'

export default {
  name: 'Movie',
  data: function () {
    return {
      selectedGenre: 1,
      movies: [],
    }
  },
  components: {
    MovieItem
  },
  methods: {
    changeSelect: function () {
      this.$store.commit('CHANGE_SELECT', this.selectedGenre)
    },
  },
  computed: {
    ...mapState(['movie_list', 'rated_movie_lst', 'selected_movie_llst']),
    ...mapGetters(['selectedMovieList'])
  },
  created: function () {

  }
}
</script>

<style>

</style>