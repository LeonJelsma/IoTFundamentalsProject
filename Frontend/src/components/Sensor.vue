<template>
    <div class="sensor" v-on:click="open">
        <div class="sensor_content">
            <div class="title">
                <h3>{{this.sensor.device_id}}</h3>
            </div>
            <p>description</p>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

	export default {
        name: "Sensor",
        props: ['sensor'],
		mounted: function () {
			this.$nextTick(function () {
				window.setInterval(() => {
					if (this.$store.state.sensor !== this.sensor)
						return;
					axios.get("http://localhost:5001/api/unit/" + this.$store.state.sensor.device_id + "/rain").then(response => {
						console.log(response);
						this.$store.commit('rain_percentage', Math.random());
					})
				},2000);
			})
		},
		methods: {
			open() {
				this.sensor.rain_percentage = 0.0;
				this.$store.commit('open_sensor', this.sensor);
			}
		}
    }
</script>

<style scoped>

    .title {
        max-height: 30%;
        width: 100%;
        font-size: 25px;
        text-align: left;
        padding-left: 5px;
        font-family: Helvetica;
        overflow: hidden;
    }

    .sensor {
        height: 140px;
        background-color: white;
        padding: 5px;
        margin-left: 10px;
        margin-right: 10px;
        margin-bottom: 10px;
        font-family: Helvetica;
        box-shadow: 0px 3px 8px 0px rgba(0, 0, 0, 0.5);
    }

    .sensor_content {
        display: inline-block;
        position: relative;
        vertical-align: top;
        width: 100%;
        height: 140px;
    }
</style>
