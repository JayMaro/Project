<template>
  <div>
    <div class="jb-box">
      <video muted autoplay loop>
        <source src="@/assets/HomeCover.mp4" type="video/mp4">
        <strong>Your browser does not support the video tag.</strong>
      </video>
      <div class="jb-text">
        <p>Welcome to MoviEver</p>
        <p @click="$router.push({name: 'Home'})" id="cover-btn" class="d-flex justify-content-center btn m-5">Go Home</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',

}
</script>

<style>

  .jb-box {
    width: 100%;
    height: 800px;
    overflow: hidden;
    margin: 0px auto;
    position: relative; 
  }
  video { 
    width: 100%;
  }
  .jb-text { 
    position: absolute; 
    top: 30%;
    width: 100%; 
  }
  .jb-text p { 
    margin-top: -24px;
    text-align: center;
    font-size: 50px;
    color: #ffffff; 
  }

  #cover-btn {
    background-color: transparent;
  }

</style>