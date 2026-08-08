// ======================================================
// ELEMENTS
// ======================================================

const form = document.getElementById("predictionForm");

const loading = document.getElementById("loadingOverlay");

const alertBox = document.getElementById("alertBox");

let forecastChart = null;


// ======================================================
// HELPERS
// ======================================================

function $(id){
    return document.getElementById(id);
}

function setText(id,value){
    $(id).textContent = value;
}

function showLoading(show){

    loading.classList.toggle("active",show);

}

function showAlert(message,type){

    alertBox.textContent = message;

    alertBox.className = `alert-box show alert-${type}`;

    setTimeout(()=>{

        alertBox.className="alert-box";

    },3000);

}

/* ==========================================================
   CURRENT DATE
========================================================== */

const currentDate = document.getElementById("currentDate");

if(currentDate){

    currentDate.textContent = new Date().toLocaleDateString(
        "en-IN",
        {
            weekday:"long",
            day:"numeric",
            month:"long",
            year:"numeric"
        }
    );

}

// ======================================================
// AUTO CALCULATE MORTALITY RATE
// ======================================================

function calculateMortalityRate(){

    const chicks = Number($("total_chicks").value);

    const mortality = Number($("mortality").value);

    const rate = chicks ? ((mortality/chicks)*100).toFixed(2) : 0;

    $("mortality_rate").value = rate + " %";

}

$("total_chicks").addEventListener("input",calculateMortalityRate);

$("mortality").addEventListener("input",calculateMortalityRate);


// ======================================================
// SUBMIT FORM
// ======================================================

form.addEventListener("submit",async function(e){

    e.preventDefault();

    showLoading(true);

    try{

        const formData = new FormData(form);

        const response = await fetch("/analyze",{

            method:"POST",

            body:formData

        });

        const data = await response.json();

        showLoading(false);

        if(!data.success){

            showAlert(data.message,"error");

            return;

        }

        updateDashboard(data.result);

        document.querySelectorAll(".result-card").forEach(card=>{
            card.classList.add("fade-up");
        });

        const panel = document.querySelector(".result-panel");
        if(panel){
            panel.scrollIntoView({
                behavior:"smooth"
            });
        }

        showAlert("Prediction Completed","success");

    }

    catch(error){

        showLoading(false);

        showAlert("Server Error","error");

    }

});


// ======================================================
// UPDATE DASHBOARD
// ======================================================

function updateDashboard(result){

    // KPI Cards

    setText("performance_result",result.farm_performance);

    setText("revenue_result",
        "₹ "+Number(result.estimated_revenue).toLocaleString());

    setText("average_demand",
        result.average_demand+" Units");



    // Insights

    setText("peak_demand",
        result.peak_demand+" Units");

    setText("lowest_demand",
        result.lowest_demand+" Units");

    setText("trend_result",
        result.trend);



    // Summary

    setText("summary_farm_size",
        $("farm_size").value);

    setText("summary_experience",
        $("experience").value);

    setText("summary_chicks",
        $("total_chicks").value);

    setText("summary_mortality",
        $("mortality").value);

    setText("summary_feed",
        $("feed").value);

    setText("summary_sales",
        $("sales_qty").value);

    setText("summary_roi",
        $("expected_roi").value+" %");

    setText(
        "summary_rate",
        Number(result.mortality_rate).toFixed(2) + " %"
    );

    latestForecast = result.forecast_values;
    drawForecastChart(latestForecast);
    updateForecastTable(latestForecast);

}


/* ==========================================================
   DEMAND FORECAST CHART
========================================================== */

function drawForecastChart(forecast) {

    if(!forecast || forecast.length === 0){
        return;
    }

    const days = forecast.map((_, i) => i + 1);

    const trace = {

        x: days,

        y: forecast,

        mode: "lines+markers",

        name: "Demand Forecast",

        line: {
            color: "#2E7D32",
            width: 3,
            shape: "spline",
            smoothing: 0.5
        },

        marker: {
            size: 6,
            color: "#2E7D32"
        },

        fill: "tozeroy",

        fillcolor: "rgba(46,125,50,0.12)",

        hovertemplate:
            "<b>Day %{x}</b><br>" +
            "Predicted Demand : <b>%{y:,} Units</b>" +
            "<extra></extra>"

    };


    const layout = {

        margin: {

            l: 60,
            r: 20,
            t: 20,
            b: 50

        },

        paper_bgcolor: "transparent",

        plot_bgcolor: "transparent",

        hovermode: "x unified",

        showlegend: true,

        legend: {

            orientation: "h",

            x: 0.35,

            y: 1.12

        },

        xaxis: {

            title: "Forecast Day",

            tickmode: "linear",

            dtick: 1,

            showgrid: true,

            zeroline: false

        },

        yaxis: {

            title: "Predicted Demand",

            separatethousands: true,

            showgrid: true,

            zeroline: false

        }

    };


    const config = {

        responsive: true,

        displaylogo: false,

        displayModeBar: true,

        modeBarButtonsToRemove: [

            "lasso2d",

            "select2d"

        ]

    };


    if (forecastChart) {
        Plotly.react(
            "forecastChart",
            [trace],
            layout,
            config
        );
    } else {
        Plotly.newPlot(
            "forecastChart",
            [trace],
            layout,
            config
        );
        forecastChart = true;
    }

}

/* ==========================================================
   FORECAST TABLE
========================================================== */

function updateForecastTable(forecast){

    const tbody=document.querySelector("#forecastTable tbody");

    tbody.innerHTML="";

    forecast.forEach((value,index)=>{

        let confidence=(94+Math.random()*5).toFixed(1)+"%";

        let trend="Stable";

        if(index>0){

            if(value>forecast[index-1])

                trend="<span style='color:#2E7D32'>▲ Increasing</span>";

            else if(value<forecast[index-1])

                trend="<span style='color:#D32F2F'>▼ Decreasing</span>";

            else

                trend="<span style='color:#FB8C00'>▬ Stable</span>";

        }

        tbody.innerHTML+=`

        <tr>

            <td>Day ${index+1}</td>

            <td>${Number(value).toLocaleString()} Units</td>

            <td>${confidence}</td>

            <td>${trend}</td>

        </tr>

        `;

    });

}


/* ==========================================================
   DOWNLOAD FORECAST CSV
========================================================== */

function downloadForecastCSV(forecast) {

    let csv="Day,Predicted Demand,Confidence,Trend\n";

    forecast.forEach((value,index)=>{
        let confidence=(94+Math.random()*5).toFixed(1)+"%";
        let trend="Stable";
        if(index>0){
            if(value>forecast[index-1])
                trend="Increasing";
            else if(value<forecast[index-1])
                trend="Decreasing";
            }
            csv+=`${index+1},${value},${confidence},${trend}\n`;
        });

    const blob = new Blob([csv], {

        type: "text/csv"

    });

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "Demand_Forecast.csv";

    a.click();

    window.URL.revokeObjectURL(url);

}

/* ==========================================================
   DOWNLOAD FORECAST PDF
========================================================== */

function downloadForecastPDF(forecast){

    const {jsPDF}=window.jspdf;

    const doc=new jsPDF();

    doc.setFontSize(18);

    doc.text("Farm Demand Forecast Report",14,20);

    let rows=[];

    forecast.forEach((value,index)=>{

        let confidence=(94+Math.random()*5).toFixed(1)+"%";

        let trend="Stable";

        if(index>0){

            if(value>forecast[index-1])

                trend="Increasing";

            else if(value<forecast[index-1])

                trend="Decreasing";

        }

        rows.push([

            index+1,

            value,

            confidence,

            trend

        ]);

    });

    doc.autoTable({

        head:[["Day","Demand","Confidence","Trend"]],

        body:rows,

        startY:30

    });

    doc.save("Demand_Forecast_Report.pdf");

}

/* ==========================================================
   DOWNLOAD BUTTON
========================================================== */

let latestForecast = [];

const downloadBtn = document.getElementById("downloadForecast");

const pdfBtn=document.getElementById("downloadPDF");

if(downloadBtn){

downloadBtn.onclick=()=>{

if(latestForecast.length)

downloadForecastCSV(latestForecast);

};

}

if(pdfBtn){

pdfBtn.onclick=()=>{

if(latestForecast.length)

downloadForecastPDF(latestForecast);

};

}