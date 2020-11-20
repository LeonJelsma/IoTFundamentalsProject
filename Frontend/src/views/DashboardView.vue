<template>
    <div>
        <TopBar>
        </TopBar>
        <div>
            <sensor-list></sensor-list>
            <div class="dashboard">
                <div class="dashboard-section">
                    <SensorInformation></SensorInformation>
                </div>
                <div class="dashboard-section">
                    <SensorMapBox></SensorMapBox>
                </div>
                <div class="dashboard-section">
                    <HistoryChart></HistoryChart>
                </div>
                <div class="dashboard-section">
                    <rain-gauge></rain-gauge>
                </div>
            </div>
        </div>
    </div>
</template>*

<script>
    import HistoryChart from "@/components/HistoryChart";
    import TopBar from "@/components/TopBar";
    import SensorList from "@/components/SensorList";
    import SensorMapBox from "@/components/SensorMapBox";
    import RainGauge from "../components/RainGauge";
    import SensorInformation from "../components/SensorInformation";

    export default {
        name: "DashboardView",
        components: {SensorInformation, RainGauge, SensorMapBox, SensorList, TopBar, HistoryChart}
    }
</script>

<style scoped>
    @import url("https://api.tiles.mapbox.com/mapbox-gl-js/v0.45.0/mapbox-gl.css");


    body {
        margin: 40px;
    }

    .dashboard{
        padding-left: 20%;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }

    .dashboard-section{
        margin: 50px;
        padding: 20px;
        min-width: 30%;
        min-height: 30%;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    
</style>
