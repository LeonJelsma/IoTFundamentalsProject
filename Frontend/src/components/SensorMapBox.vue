<template>
    <div class="wrapper">
        <MglMap id="mapbox" class="map" :accessToken="accessToken" :mapStyle="mapStyle" ref="mapbox">
            <MglMarker :coordinates="coordinates" color="blue">
                <MglPopup>
                    <div class="card">
                        <div>Hello, I'm popup!</div>
                    </div>
                </MglPopup>
            </MglMarker>
        </MglMap>
    </div>
</template>

<script>
    import {MglMap, MglMarker, MglPopup} from "vue-mapbox";

    export default {
        name: "SensorMapBox",
        components: {MglMap, MglMarker, MglPopup},
        mounted() {
            console.log(this.$refs.mapbox)
            this.$refs.mapbox.mapObject.flyTo(this.coordinates)
        },
        data() {
            return {
                coordinates: [6.5665, 53.2194],
                accessToken: "pk.eyJ1IjoibGVvbnZpcnVzIiwiYSI6ImNrZ25kbzk5ZzBmN2gyeW13Z3dyanUweDIifQ.GksPDMvlIUUFOtrXrNLFcg",
                mapStyle: "mapbox://styles/mapbox/light-v10"
            }
        },
    }
</script>

<style scoped>

    .wrapper {
        margin: auto;
        height: 500px;
        width: 500px;
    }

    .map {
        margin: auto;
        width: 500px;
        height: 500px;
    }
</style>
