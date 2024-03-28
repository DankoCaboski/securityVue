<script setup>
import { RouterLink, RouterView } from 'vue-router'


  const toLinkedin = () => {
    window.open('https://www.linkedin.com', '_blank')
  
}

</script>

<template>



</template>

<style scoped>

  .octicon.octicon-mark-github path {
      filter: invert(1);
  }
  
#header {
  width: 100%;
  height: 100%;
  margin-left: 0;
}

#footer {
  background-color: #887f87;
  width: auto;
  font-size: 12px;
  text-align: center;
  margin-bottom: 0;
}

#main{
  background-color: #f8f9fa;
  width: 100%;
  height: 100%;
  margin-left: 0;
  margin-bottom: 0;

}
body {
   display: flex;
   flex-direction: column;
   min-height: 100vh;
   justify-content: space-between;
}

nav {
  background-color: #8b6085;
  width: 100%;
  font-size: 12px;
  text-align: center;
}

</style>

