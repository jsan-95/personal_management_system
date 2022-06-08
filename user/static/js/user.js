new Vue({
      el: '#profile',
      delimiters: ['${','}'],
      data: {
        user: null,
        userForm: {},
        editMode: false,
        loading: false,
        message: null,
      },
      beforeCreate (){
          if (!localStorage.user) {
            window.location.href = "/login";
          }
      },
      mounted: function() {
        this.user = JSON.parse(localStorage.user);
        this.userForm = {
            user_id: this.user.id,
            name: this.user.name,
            first_name: this.user.first_name,
            last_name: this.user.last_name,
            email: this.user.email,
            password: null,
            password2: null,
            avatar: null,
        }
      },
      methods: {
        updateUser: function() {
          this.loading = true;
          if (this.userForm.password && this.userForm.password !== this.userForm.password2){
            this.message = "Passwords are different";
            this.loading = false;
            return;
          }
          const input = $("#avatar")[0];

          if (input.files && input.files[0]) {
                this.userForm.avatar = $("#avatar_url")[0].src;
          }

          this.$http.post(`/update_user`, this.userForm)
            .then((response) => {
                localStorage.user = JSON.stringify(response.data);
                window.location.reload();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
                this.message = "Error. Try again";
              })
        },
        readURL() {
            const input = $("#avatar")[0];
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#avatar_url')
                        .attr('src', e.target.result);
                };

                reader.readAsDataURL(input.files[0]);
            }
        },
        logout() {
            this.loading = true;
            this.$http.get("/logout")
              .then((response) => {
                delete localStorage.user;
                window.location.href = "/login";
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        }
      }
    });