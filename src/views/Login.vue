<script>
export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        login(event) {
            event.preventDefault();
            // Perform login logic here
            console.log('Username:', this.username);
            console.log('Password:', this.password);
            // Reset form fields
            this.username = '';
            this.password = '';
        }
    }
};
</script>

<template>
    <div>
        <h1>Login</h1>
        <form @submit="login">
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" required>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</template>


<style scoped>
/* Add your custom styles here */
</style>