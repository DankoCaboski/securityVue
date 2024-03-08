<script setup>
import { RouterLink, RouterView } from 'vue-router'


  const toLinkedin = () => {
    window.open('https://www.linkedin.com', '_blank')
  
}

</script>

<template>


  <div id="header">

    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Pricing</a>
            </li>
            <li class="nav-item">
              <router-link to="/auth" class="nav-link">Login</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

  </div>

  <div id="main">

  </div>

     

<!-- Footer -->
<div id="footer">
  <p>&copy; 2023 Willian Caboski</p>
    <svg id="octocat" height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
        <defs>
        </defs>
        <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
    </svg>
</div>

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

