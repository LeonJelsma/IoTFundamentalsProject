<template>
    <div class="sensor_list">
        <sensor v-for="sensor in sensorList" :key="sensor.device_id" :sensor="sensor"></sensor>
    </div>
</template>

<script>
    import axios from "axios";
    import Sensor from "@/components/Sensor";
    export default {
        name: "SensorList",
        data: function () {
            return {
                sensorList: []
            };
        },
        beforeCreate: function () {
            axios.get("http://localhost:5001/api/unit").then(response => {
                this.sensorList = response.data;
            })
        },
        components: {Sensor}
    }
</script>

<style scoped>
    .sensor_list{
        width: 20%;
        height: 94%;
        max-height: 94%;
        position: absolute;
        overflow: scroll;
        overflow-x: hidden
    }
</style>
