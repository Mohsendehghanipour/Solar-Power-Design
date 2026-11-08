
# =====================================================
# نرم افزار هوشمند پيش بيني توان نيروگاه خورشيدي
# Machine Learning - Random Forest
# =====================================================


# -----------------------------------------------------
# 1. وارد کردن کتابخانه ها
# -----------------------------------------------------

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path
import webbrowser
import html


# -----------------------------------------------------
# 2. تعريف داده هاي آموزشي
# -----------------------------------------------------

data = {

    "radiation": [200, 300, 400, 500, 600, 700, 800, 900, 1000],

    "temperature": [20, 22, 24, 25, 27,28, 30, 32, 35],

    "tilt": [20, 20, 25, 25, 30, 30, 30, 35, 35],

    "power": [10, 15, 20, 25, 30, 35, 40, 45, 50]
}


# -----------------------------------------------------
# 3. تبديل داده ها به جدول
# -----------------------------------------------------

df = pd.DataFrame(data)


# -----------------------------------------------------
# 4. تعيين ورودي و خروجي مدل
# -----------------------------------------------------

X = df[["radiation", "temperature", "tilt"]]

y = df["power"]


# -----------------------------------------------------
# 5. ساخت مدل يادگيري ماشين
# -----------------------------------------------------

model = RandomForestRegressor(

    n_estimators=100,

    random_state=50

)


# -----------------------------------------------------
# 6. آموزش مدل
# -----------------------------------------------------

model.fit(X, y)


# -----------------------------------------------------
# 7. ورود اطلاعات جديد براي پيش بيني
# -----------------------------------------------------

new_data = pd.DataFrame({

    "radiation": [750],

    "temperature": [45],

    "tilt": [34]

})


# -----------------------------------------------------
# 8. انجام پيش بيني توان
# -----------------------------------------------------

prediction = model.predict(new_data)


# -----------------------------------------------------
# 9. استخراج اطلاعات ورودي و خروجي
# -----------------------------------------------------

radiation = new_data["radiation"].iloc[0]

temperature = new_data["temperature"].iloc[0]

tilt = new_data["tilt"].iloc[0]

power = float(prediction[0])


# -----------------------------------------------------
# 10. نمايش گزارش در محيط پایتون
# -----------------------------------------------------

print()

print("==============================================")

print("گزارش پيش بيني نيروگاه خورشيدي")

print("==============================================")

print()

print("میزان تابش خورشیدی:", radiation, "W/m²")

print()

print("دمای محیط:", temperature, "°C")

print()

print("زاویه تیلت پنل:", tilt, "درجه")

print()

print("توان پیش بینی شده:", round(power, 2), "kW")

print()

print("==============================================")


# -----------------------------------------------------
# 11. ساخت گزارش HTML
# -----------------------------------------------------

report_html = """

<!DOCTYPE html>

<html lang="fa" dir="rtl">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>گزارش پیش بینی نیروگاه خورشیدی</title>


<style>

body {

    font-family: Tahoma, Arial, sans-serif;

    direction: rtl;

    background: #f2f4f8;

    margin: 0;

    padding: 30px;

    color: #263238;

}


.report {

    max-width: 750px;

    margin: auto;

    background: white;

    padding: 30px;

    border-radius: 12px;

    box-shadow: 0 3px 15px #cccccc;

}


h2 {

    text-align: center;

    color: #174a70;

    border-bottom: 2px solid #174a70;

    padding-bottom: 20px;

}


h3 {

    color: #174a70;

}


table {

    width: 100%;

    border-collapse: collapse;

    margin-top: 25px;

}


th, td {

    border: 1px solid #d5dce2;

    padding: 15px;

    text-align: right;

}


th {

    background: #eaf1f6;

}


.value {

    direction: ltr;

    text-align: left;

    font-weight: bold;

}


.result {

    margin-top: 25px;

    padding: 20px;

    background: #e7f5eb;

    border-radius: 8px;

    text-align: center;

}


.result h3 {

    color: #176b36;

}


.power {

    font-size: 32px;

    color: #176b36;

    font-weight: bold;

    direction: ltr;

}


.footer {

    text-align: center;

    margin-top: 30px;

    color: #777;

    font-size: 12px;

    line-height: 2;

}


button {

    display: block;

    margin: 25px auto;

    padding: 12px 30px;

    background: #174a70;

    color: white;

    border: none;

    border-radius: 6px;

    cursor: pointer;

    font-size: 15px;

}


@media print {

    body {

        background: white;

        padding: 0;

    }

    .report {

        box-shadow: none;

    }

    button {

        display: none;

    }

}

</style>

</head>


<body>


<div class="report">


<h2>

گزارش هوشمند پیش بینی توان نیروگاه خورشیدی

</h2>


<h3>۱- مشخصات ورودی سیستم</h3>


<table>

<tr>

<th>پارامتر</th>

<th>مقدار</th>

</tr>


<tr>

<td>شدت تابش خورشیدی</td>

<td class="value">@@RADIATION@@ W/m²</td>

</tr>


<tr>

<td>دمای محیط</td>

<td class="value">@@TEMPERATURE@@ °C</td>

</tr>


<tr>

<td>زاویه تیلت پنل</td>

<td class="value">@@TILT@@ °</td>

</tr>


</table>


<div class="result">


<h3>۲- نتیجه پیش بینی مدل یادگیری ماشین</h3>


<div class="power">

@@POWER@@ kW

</div>


<p>توان پیش بینی شده نیروگاه خورشیدی</p>


</div>


<div class="footer">

گزارش تولید شده توسط سامانه هوشمند پیش بینی نیروگاه خورشیدی

<br>

الگوریتم: Random Forest Regressor

<br>

Machine Learning System

</div>


<button onclick="window.print()">

چاپ گزارش / ذخیره PDF

</button>


</div>


</body>

</html>

"""


# -----------------------------------------------------
# 12. جايگزيني مقادير واقعي در گزارش
# -----------------------------------------------------

report_html = report_html.replace(

    "@@RADIATION@@",

    html.escape(str(radiation))

)


report_html = report_html.replace(

    "@@TEMPERATURE@@",

    html.escape(str(temperature))

)


report_html = report_html.replace(

    "@@TILT@@",

    html.escape(str(tilt))

)


report_html = report_html.replace(

    "@@POWER@@",

    f"{power:.2f}"

)


# -----------------------------------------------------
# 13. ذخيره گزارش HTML
# -----------------------------------------------------

report_path = Path(__file__).with_name(

    "solar_report.html"

)


report_path.write_text(

    report_html,

    encoding="utf-8"

)


# -----------------------------------------------------
# 14. باز کردن گزارش در مرورگر
# -----------------------------------------------------

webbrowser.open(

    report_path.resolve().as_uri()

)


# -----------------------------------------------------
# 15. پايان برنامه
# -----------------------------------------------------

print()

print("گزارش مهندسی با موفقیت ایجاد شد.")

print()

print("مسیر ذخیره گزارش:")

print(report_path)

print()

print("برنامه با موفقیت اجرا شد.")

