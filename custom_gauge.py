import streamlit as st
import streamlit.components.v1 as components

def render_gauge(value):
    components.html('''
    <style>
    #wrapper {
      position: relative;
      margin: auto;
    }
    #meter {
      width: 100%; height: 100%;
      transform: rotateX(180deg);
    }
    .circle {
      fill: none;
    }
    .outline, #mask {
      stroke: #F1F1F1;
      stroke-width: 65;
    }
    .range {
      stroke-width: 60;
    }
    #lbl {
        border-radius: 2px;
        color: #777777;
        font-family: 'courier new';
        font-size: 65pt;
        font-weight: bold;
        padding: 4px 4px 2px 4px;
        right: 0%;
        margin: auto;
        left: 0%;
        position: absolute;
        top: 150px;
        text-align: center;
    }

    </style>

    <div id="wrapper">
        <svg id="meter">
            <circle id="outline_curves" class="circle outline"
            cx="50%" cy="50%"></circle>

            <circle id="low" class="circle range" cx="50%" cy="50%"
            stroke="#FDE47F"></circle>

            <circle id="avg" class="circle range" cx="50%" cy="50%"
            stroke="#FDC45F"></circle>

            <circle id="high" class="circle range" cx="50%" cy="50%"
            stroke="#FF340F"></circle>

            <circle id="mask" class="circle" cx="50%" cy="50%" >
            </circle>

            <circle id="outline_ends" class="circle outline"
            cx="50%" cy="50%"></circle>
        </svg>
        <label id="lbl" id="value" for="">0</label>
    </div>

    <script>
    /* Set radius for all circles */
    var r = 250;
    var circles = document.querySelectorAll('.circle');
    var total_circles = circles.length;
    for (var i = 0; i < total_circles; i++) {
        circles[i].setAttribute('r', r);
    }

    /* Set meter's wrapper dimension */
    var meter_dimension = (r * 2) + 100;
    var wrapper = document.querySelector("#wrapper");
    wrapper.style.width = meter_dimension + "px";
    wrapper.style.height = meter_dimension + "px";

    /* Add strokes to circles  */
    var cf = 2 * Math.PI * r;
    var semi_cf = cf / 2;
    var semi_cf_1by3 = semi_cf / 3;
    var semi_cf_2by3 = semi_cf_1by3 * 2;
    document.querySelector("#outline_curves").setAttribute("stroke-dasharray", semi_cf + "," + cf);
    document.querySelector("#low").setAttribute("stroke-dasharray", semi_cf + "," + cf);
    document.querySelector("#avg").setAttribute("stroke-dasharray", semi_cf_2by3 + "," + cf);
    document.querySelector("#high").setAttribute("stroke-dasharray", semi_cf_1by3 + "," + cf);
    document.querySelector("#outline_ends").setAttribute("stroke-dasharray", 2 + "," + (semi_cf - 2));
    document.querySelector("#mask").setAttribute("stroke-dasharray", semi_cf + "," + cf);

    var lbl = document.querySelector("#lbl");
    var mask = document.querySelector("#mask");

    function update_gauge(percent) {
        var meter_value = semi_cf - ((percent * semi_cf) / 100);
        mask.setAttribute("stroke-dasharray", meter_value + "," + cf);

     lbl.textContent = percent + "%";
    }
    update_gauge(''' + str(value) + ''');
    </script>
    ''', height = 350)
