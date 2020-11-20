<template>
    <div>
       <table>
           <tr>
               <td colspan="2" class="table-title">
                   Selected Sensor
               </td>
           </tr>
           <tr class="table-row">
               <td class="table-key">
                   Name:
               </td>
               <td class="table-value">
                    {{sensor_name}}
               </td>
           </tr>
           <tr class="table-row">
               <td class="table-key">
                   Description:
               </td>
               <td class="table-value">
                   {{this.sensorInformation.description}}
               </td>
           </tr>
           <tr class="table-row">
               <td class="table-key">
                   Location:
               </td>
               <td class="table-value">
                   {{this.sensorInformation.location}}
               </td>
           </tr>
       </table>
    </div>
</template>

<script>
    export default {
        name: "SensorInformation",
        data() {
            return {
                sensorInformation: {
                    name: "Sensor 1",
                    description: "Erg mooie sensor",
                    location: "Groningen",
                }
            }
        },
		computed: {
			sensor_name() {
				return this.$store.state.sensor.device_id
			}
		}
    }
</script>

<style scoped>
    table {
        width: 100%;
        padding: 30px;
    }

    .table-row {
        border-bottom: 2px dashed grey;
    }

    .table-title {
        font-size: 40px;
    }

    .table-key {
        float: left;
        vertical-align: bottom;
        font-size: 30px;
    }

    .table-value {
        float: right;
        vertical-align: text-bottom;
        font-size: 20px
    }
</style>
