new Vue({
      el: '#login-page',
      delimiters: ['${','}'],
      data: {
        loading: false,
        message: null,
        userLogin: {
            'email': null, 'password': null
            },
      },
      methods: {
        login: function() {
          this.loading = true;
          this.$http.post("/login/auth", this.userLogin)
              .then((response) => {
                this.loading = false;
                this.message = "";
                localStorage.user = JSON.stringify(response.data);
                window.location.href = "/user";
              })
              .catch((err) => {
                this.loading = false;
                this.message = "Error in login";
              })
        }
      }
    });