<template>
    <div class="gauge">
        <svg id="gauge" height="180" width="300">
            <defs>
                <mask id="donut">
                    <path d="M 0 150
           A 45 45, 0, 0, 1, 300 150
           L 230 150
           A 45 45, 0, 0, 0, 70, 150
           L 0 150" fill="white" stroke="black"/>
                </mask>
            </defs>

            <path d="M 0 150
           A 45 45, 0, 0, 1, 300 150
           L 230 150
           A 45 45, 0, 0, 0, 70, 150
           L 0 150" fill="white" stroke="#BBBBBB"/>

            <g mask="url(#donut)">
                <rect x="0" y="150"
                      height="150" width="300"
                      :fill="this.color"
                      :transform="`rotate(${this.rotation} 150 150)`"/>
            </g>

            <text class="rate" x="150" y="135" text-anchor="middle">{{ chance | percentage }}</text>
            <text class="label" x="150" y="180" text-anchor="middle">{{ label }}</text>
        </svg>
    </div>
</template>

<script>
    export default {
        name: "RainGauge",
        el: '#gauge',
        data() {
            return {
                label: 'Risk of rain',
                colors: [
                    {pct: 0.0, color: {r: 0x00, g: 0xff, b: 0}},
                    {pct: 0.5, color: {r: 0xff, g: 0xff, b: 0}},
                    {pct: 1.0, color: {r: 0xff, g: 0x00, b: 0}}]
            }
        },
        computed: {
			chance() {
				console.log(this.$store.state.sensor.rain_percentage)
				return this.$store.state.sensor.rain_percentage
			},
            rotation() {
                return this.scale(this.$store.state.sensor.rain_percentage, 1, 180)
            },
            color() {
                return this.getColorForPercentage(this.$store.state.sensor.rain_percentage)
            },
        },
        methods: {
            scale(n, domainMax, rangeMax) {
                const rate = n / domainMax;
                return rangeMax * rate;
            },
            componentToHex(c) {
                var hex = c.toString(16);
                return hex.length == 1 ? "0" + hex : hex;
            },
            getColorForPercentage(pct) {
                for (var i = 1; i < this.colors.length - 1; i++) {
                    if (pct < this.colors[i].pct) {
                        break;
                    }
                }
                var lower = this.colors[i - 1];
                var upper = this.colors[i];
                var range = upper.pct - lower.pct;
                var rangePct = (pct - lower.pct) / range;
                var pctLower = 1 - rangePct;
                var pctUpper = rangePct;
                var color = {
                    r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
                    g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
                    b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper)
                };
                var test = "#" + this.componentToHex(color.r) + this.componentToHex(color.g) + this.componentToHex(color.b)
                console.log(test);
                return "#" + this.componentToHex(color.r) + this.componentToHex(color.g) + this.componentToHex(color.b);
            }
        },
        filters: {
            percentage: n => `${(n * 100).toFixed(1)}%`,
        }
    }
</script>

<style scoped>

    .gauge {
        margin: auto;
        padding: 50px
    }

    html, body {
        height: 100%;
    }

    body {
        display: grid;
        margin: 0;
    }

    svg {
        margin: auto;
    }

    svg text {
        font-family: Roboto;
    }

    svg text.label {
        font-size: 22px;
    }

    svg text.rate {
        font-weight: bold;
        font-size: 35px;
    }
</style>
