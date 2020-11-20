<template>
    <b-navbar class="nav-bar-custom" :transparent="true" :centered="true">
        <template slot="brand">
            <b-navbar-item>
                <img
                        src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
                >
            </b-navbar-item>
        </template>
        <template slot="start">
            <b-navbar-item>
                <h5 class="title">
                    Sensor Dashboard
                </h5>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
    export default {
        name: "TopBar"
    }
</script>

<style scoped lang="scss">
    $navbar-height: 5rem;

    @import "~bulma/bulma";

    .nav-bar-custom {
        height: 50%;
        background-color: green;
    }

    .title {
        color: black;
    }

    b-navbar {

    }
</style>
