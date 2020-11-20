import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import 'leaflet/dist/leaflet.css'
import VueMapbox from "vue-mapbox"
import Mapbox from "mapbox-gl"
import 'mapbox-gl/dist/mapbox-gl.css'

Vue.use(VueMapbox, {mapboxgl: Mapbox})
Vue.use(Buefy)
Vue.use(Vuex)
Vue.config.productionTip = false

const store = new Vuex.Store({
	state: {
		sensor: {
			device_id: "NONE",
			rain_percentage: 0.5
		}
	},
	mutations: {
		open_sensor(state, sensor) {
			state.sensor = sensor
		},
		rain_percentage(state, rain_percentage) {
			state.sensor.rain_percentage = rain_percentage
		}
	}
})

new Vue({
	store: store,
	render: h => h(App),
}).$mount('#app')