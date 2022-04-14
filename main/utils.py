from xhtml2pdf import pisa
from django.core.mail import EmailMessage
import io


SOURCE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MasterCleaner Report</title>

    <!-- Bootstrap CSS -->
    <style>
        .logo {
            display: flex;
            justify-content: space-between;
        }
        .logo img {
            width: 480px;
            height: 110px;
        }
        h2, h4 {
            font-weight: 400;
        }
        .header, .contact-info {
            margin-bottom: 5em;
        }
        .customer-info .basic h4 {
            font-weight: bolder;
        }
        .customer-info .basic .placeholders {
            margin-left: 2.5em;
            line-height: 5px;
        }
        .underline {
            text-decoration: underline !important;
        }
        .thank-you {
            background: linear-gradient(#ffffff, #c7d5e8);
            height: 100px;
            margin-bottom: 1.5em;
        }
        .thank-you h3 {
            padding-top: 50px;
        }
        .thank-you hr {
            height: 5px;
            color: #6683ad;
        }

        .table {
            width: 100%;
            margin: 2em 0 2em 0;
        }
        .table thead th {
            font-size: 16px;
        }
        .table th, tr, td {
            border: 1px solid lightgray;
        }
    </style>
</head>
<body class="container">
    <div class="logo">
        <img src="https://i.imgur.com/BT6GFNC.jpg" alt="Logo">
        <h2>QUOTE</h2>
    </div>
    <div class="header">
        <h2>PROPERTY SERVICES</h2>
        <h2>CELEBRATING 25 YEARS!</h2>
    </div>
    
    <div class="contact-info">
        <h4>TOLL-FREE: 1-855-SEALED-0</h4>
        <h4>905 Region: 905-850-8955</h4>
        <h4>416 Region: 416-450-1157</h4>
        <h4>service@mastersealer.com</h4>
        <h4>www.mastersealer.com</h4>
    </div>

    <div class="customer-info">
        <div class="basic">
            <h4>TO:</h4>
            <div class="placeholders">
                <p>[COMPANY_NAME]</p>
                <p>[NAME]</p>
                <p>[ADDRESS]</p>
                <p>[CITY]</p>
            </div>
        </div>

        <div class="quotation">
            <table class="table">
                <thead>
                    <th>Estimator</th>
                    <th>Quotation #</th>
                    <th>Payment Structure</th>
                    <th>Quotation Date</th>
                </thead>
                <tbody>
                    <tr>
                        <td>[ESTIMATOR]</td>
                        <td>[QUOTATION]</td>
                        <td>[PAYMENT_STRUCTURE]</td>
                        <td>[QUOTATION_DATE]</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <hr>
        
        <div class="services">
            <table class="table">
                <thead>
                    <th>QTY</th>
                    <th>DESCRIPTION OF SERVICES</th>
                    <th>AREA</th>
                    <th>TOTAL</th>
                </thead>
                <tbody>
                    <tr>
                        <td>[QTY1]</td>
                        <td>[DESC1]</td>
                        <td>[AREA1]</td>
                        <td>[TOTAL1]</td>
                    </tr>

                    <tr>
                        <td>[QTY2]</td>
                        <td>[DESC2]</td>
                        <td>[AREA2]</td>
                        <td>[TOTAL2]</td>
                    </tr>

                    <tr>
                        <td>[QTY3]</td>
                        <td>[DESC3]</td>
                        <td>[AREA3]</td>
                        <td>[TOTAL3]</td>
                    </tr>

                    <tr>
                        <td>[QTY4]</td>
                        <td>[DESC4]</td>
                        <td>[AREA4]</td>
                        <td>[TOTAL4]</td>
                    </tr>

                    <!-- TOTALS -->
                    <tr>
                        <td></td>
                        <td></td>
                        <td class="bg-success text-white">Subtotal</td>
                        <td class="bg-success text-white">[SUBTOTAL]</td>
                    </tr>

                    <tr>
                        <td></td>
                        <td></td>
                        <td class="bg-success text-white">HST</td>
                        <td class="bg-success text-white">[HST]</td>
                    </tr>

                    <tr>
                        <td></td>
                        <td></td>
                        <td class="bg-success text-white">Total</td>
                        <td class="bg-success text-white">[TOTAL]</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="credit">
            <p>Quotation prepared by: <span class="underline">[ESTIMATOR]</span></p>
            <p>If you would like to accept this quotation or if you have any questions, please call or email: 905-850-8955 - Service@mastersealer.com</p>

            <div class="thank-you">
                <h3 class="text-center">THANK YOU FOR THE OPPORTUNITY OF DOING BUSINESS!</h3>
                <hr>
            </div>
        </div>

    </div>
        
</body>
</html>
"""


def send_email(params: dict):
    global SOURCE_HTML
    SOURCE_HTML = SOURCE_HTML.replace("[COMPANY_NAME]", params.get('company'))
    SOURCE_HTML = SOURCE_HTML.replace("[NAME]", params.get('name'))
    SOURCE_HTML = SOURCE_HTML.replace("[EMAIL]", params.get('email'))
    SOURCE_HTML = SOURCE_HTML.replace("[ADDRESS]", params.get('address'))
    SOURCE_HTML = SOURCE_HTML.replace("[CITY]", params.get('city'))
    # SOURCE_HTML.replace("[COMPANY]", params.get('postal_code'))

    SOURCE_HTML = SOURCE_HTML.replace("[ESTIMATOR]", params.get('estimator'))
    SOURCE_HTML = SOURCE_HTML.replace("[QUOTATION]", params.get('quotation'))
    SOURCE_HTML = SOURCE_HTML.replace("[PAYMENT_STRUCTURE]", params.get('payment_structure'))
    SOURCE_HTML = SOURCE_HTML.replace("[QUOTATION_DATE]", params.get('quotation_date'))
    
    SOURCE_HTML = SOURCE_HTML.replace("[QTY1]", '')
    SOURCE_HTML = SOURCE_HTML.replace("[DESC1]", params.get('desc1'))
    SOURCE_HTML = SOURCE_HTML.replace("[AREA1]", params.get('area1'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL1]", params.get('price1'))

    SOURCE_HTML = SOURCE_HTML.replace("[QTY2]", '')
    SOURCE_HTML = SOURCE_HTML.replace("[DESC2]", params.get('desc2'))
    SOURCE_HTML = SOURCE_HTML.replace("[AREA2]", params.get('area2'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL2]", params.get('price2'))

    SOURCE_HTML = SOURCE_HTML.replace("[QTY3]", '')
    SOURCE_HTML = SOURCE_HTML.replace("[DESC3]", params.get('desc3'))
    SOURCE_HTML = SOURCE_HTML.replace("[AREA3]", params.get('area3'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL3]", params.get('price3'))

    SOURCE_HTML = SOURCE_HTML.replace("[QTY4]", '')
    SOURCE_HTML = SOURCE_HTML.replace("[DESC4]", params.get('desc4'))
    SOURCE_HTML = SOURCE_HTML.replace("[AREA4]", params.get('area4'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL4]", params.get('price4'))

    SOURCE_HTML = SOURCE_HTML.replace("[SUBTOTAL]", params.get('subtotal'))
    SOURCE_HTML = SOURCE_HTML.replace("[HST]", params.get('hst'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL]", params.get('total'))
    
    send_to_customer = params.get('emailreport')
    recipients = ['info@mastercleaner.com']

    if send_to_customer == 1:
        recipients.append(params.get('email'))

    buf = io.BytesIO()
    pisa.CreatePDF(SOURCE_HTML, dest=buf)
    buf.seek(0)

    email = EmailMessage(subject="Testing", body="<h1>Testing 123</h1>", to=recipients)
    email.content_subtype = 'html'
    email.attach(filename="master-cleaner.pdf", content=buf.read())
    email.send()
