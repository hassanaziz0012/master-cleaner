from xhtml2pdf import pisa
from django.core.mail import EmailMessage
import io


def send_email(params: dict):
    SOURCE_HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Master Sealer Report</title>

    <!-- Bootstrap CSS -->
    <style>
        h2,
        h4 {
            font-weight: 400;
            line-height: 0.1px;
        }

        .customer-info .basic h4 {
            font-weight: bolder;
            line-height: 0.1px;
        }

        .customer-info .basic .placeholders {
            margin-left: 2.5em;
            line-height: 0.1px;
        }

        .contact-info * {
            margin-top: 15px;
            margin-bottom: 15px;
        }

        .underline {
            text-decoration: underline !important;
        }

        .quotation .table tr > td {
            padding-top: 10px;
        }

        .thank-you {
            background: #c7d5e8;
            height: 50px;
            margin-bottom: 1em;
            text-align: center;
        }
        
        .thank-you h3 {
            padding-top: 17.5px;
        }
        .credit p {
            line-height: 1px;
        }

        .table {
            width: 100%;
            margin: 1em 0 0 0;
            border-collapse: separate;
        }

        .quotation .table {
            border-bottom: 1px solid lightgray;
        }

        .table thead th {
            font-size: 12px;
            background-color: #c7d5e8;
            border: 1.5px solid darkgray;
            padding: 0.5em;
        }
        
        .table td {
            text-align: center;
        }

        .table tr td {
            border-left: 1px solid lightgray;
        }
        .table tr td.no-border {
            border-left: none;
        }

        .totals-table {
            float: right;
            margin-left: auto;
        }

        .border-row {
            border: 1px solid lightgray;
        }

        .border-bottom-row {
            border-bottom: 1px solid lightgray;
        }
        .border-bottom-row > td {
            padding-bottom: 1em;
        }
        .padding-top-row > td {
            padding-top: 1em;
        }

        .quantity-cell {
            width: 40px;
        }
        .first-row {
            padding-top: 2em;
        }
        .service-row * {
            padding-top: 1em;
        }
        .area-header, .total-header {
            width: 100px;
        }

        .flexrow {
            display: -webkit-box;
            display: -webkit-flex;
            display: flex;
        }
        .flexrow > div {
            -webkit-box-flex: 1;
            -webkit-flex: 1;
            flex: 1;
            margin-right: 10%;
            background-color: yellow;
            border: 1px dashed black;
        }
        .flexrow > div:last-child {
            margin-right: 0;
        }
        .text-center {
            text-align: center;
        }

    </style>
</head>

<body class="container">
    <div class="logo flexrow">
        <img src="https://i.imgur.com/qrS1Olx.png" alt="Logo">
    </div>
    <br>

    <br>
    <div class="contact-info" style="font-size: 12px;">
        <p style="margin: 0 0; padding: 0 0;">TOLL-FREE: 1-855-SEALED-0</p>
        <p style="margin: 0 0; padding: 0 0;">905 Region: 905-850-8955</p>
        <p style="margin: 0 0; padding: 0 0;">416 Region: 416-450-1157</p>
        <p style="margin: 0 0; padding: 0 0;">service@mastersealer.com</p>
        <p style="margin: 0 0; padding: 0 0;">www.mastersealer.com</p>
    </div>
    <br>
    
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
                    <th>ESTIMATOR</th>
                    <th>QUOTATION #</th>
                    <th>PAYMENT STRUCTURE</th>
                    <th>QUOTATION DATE</th>
                </thead>
                <tbody>
                    <tr>
                        <td>[ESTIMATOR]</td>
                        <td>[QUOTATION]</td>
                        <td>[PAYMENT_STRUCTURE]</td>
                        <td style="border-right: 1px solid lightgray;">[QUOTATION_DATE]</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="services">
            <table class="table">
                <thead>
                    <th>QTY</th>
                    <th style="width: 800px">DESCRIPTION OF SERVICES</th>
                    <th class="area-header">AREA</th>
                    <th class="total-header">TOTAL</th>
                </thead>
                <tbody>
                    <tr class="service-row">
                        <td class="quantity-cell first-row" style="width: 50px;">[QTY1]</td>
                        <td class="first-row" style="width: 800px; text-align: left; padding-left: 1em;">[DESC1]</td>
                        <td class="first-row" style="width: 100px;">[AREA1]</td>
                        <td class="first-row" style="border-right: 1px solid lightgray; font-weight: bold; width: 100px;">[TOTAL1]</td>
                    </tr>

                    <tr class="service-row">
                        <td class="quantity-cell">[QTY2]</td>
                        <td style="text-align: left; padding-left: 1em;">[DESC2]</td>
                        <td>[AREA2]</td>
                        <td style="border-right: 1px solid lightgray; font-weight: bold;">[TOTAL2]</td>
                    </tr>

                    <tr class="service-row">
                        <td class="quantity-cell">[QTY3]</td>
                        <td style="text-align: left; padding-left: 1em;">[DESC3]</td>
                        <td>[AREA3]</td>
                        <td style="border-right: 1px solid lightgray; font-weight: bold;">[TOTAL3]</td>
                    </tr>

                    <tr class="border-bottom-row service-row">
                        <td class="quantity-cell">[QTY4]</td>
                        <td style="text-align: left; padding-left: 1em;">[DESC4]</td>
                        <td>[AREA4]</td>
                        <td style="border-right: 1px solid lightgray; font-weight: bold;">[TOTAL4]</td>
                    </tr>

                    <!-- TOTALS -->
                    <tr class="padding-top-row">
                        <td class="no-border"></td>
                        <td class="no-border"></td>
                        <td class="no-border" style="text-align: right; padding-right: 5px;"><b>SUBTOTAL</b></td>
                        <td class="border-row" style="font-weight: bold;">[SUBTOTAL]</td>
                    </tr>

                    <tr class="padding-top-row">
                        <td class="no-border"></td>
                        <td class="no-border"></td>
                        <td class="no-border" style="text-align: right; padding-right: 5px;"><b>HST</b></td>
                        <td class="border-row" style="font-weight: bold;">[HST]</td>
                    </tr>

                    <tr class="padding-top-row">
                        <td class="no-border"></td>
                        <td class="no-border"></td>
                        <td class="no-border" style="text-align: right; padding-right: 5px;"><b>TOTAL</b></td>
                        <td class="border-row" style="font-weight: bold;">[TOTAL]</td>
                    </tr>

                </tbody>
            </table>
        </div>

        <div class="credit">
            <p>Quotation prepared by: <span class="underline">[ESTIMATOR]</span></p>
            <p>If you would like to accept this quotation, simply reply to this email for the quickest response.</p>

            <div class="thank-you">
                <h3 class="text-center">THANK YOU FOR THE OPPORTUNITY OF DOING BUSINESS!</h3>
            </div>

        </div>

    </div>

</body>

</html>
    """

    EMAIL_BODY = """
    <p>Hi,</p>
    <br>
    <p>[CUSTOMER_NAME] has created a new estimate.</p>
    <br>
    <p>
    Please find your estimate attached to this email.
    <br>
    Please let me know if you have any questions or would like to schedule a start date.
    </p>
    <br>
    <p>Thank you, John</p>
    <br>
    <p>
    Master Sealer Property Services <br>
    www.MasterSealer.com <br>
    service@mastersealer.com <br>
    905-850-8955 <br>
    416-450-1157 <br>
    </p>
    <br>
    <p>The best compliment that you can give our company is a referral.</p>
    """

    def get_price(price):
        if price == '0.0' or price == '0' or price == '0.00':
            return ''
        elif '.' in price:
            return '$    ' + price
        else:
            return '$    ' + price + '.00'


    SOURCE_HTML = SOURCE_HTML.replace("[COMPANY_NAME]", params.get('company'))
    SOURCE_HTML = SOURCE_HTML.replace("[NAME]", params.get('name'))
    SOURCE_HTML = SOURCE_HTML.replace("[EMAIL]", params.get('email'))
    SOURCE_HTML = SOURCE_HTML.replace("[ADDRESS]", params.get('address'))
    SOURCE_HTML = SOURCE_HTML.replace("[CITY]", params.get('city'))
    # SOURCE_HTML.replace("[COMPANY]", params.get('postal_code'))

    SOURCE_HTML = SOURCE_HTML.replace("[ESTIMATOR]", params.get('estimator'))
    if params.get('quotation') != '':
        SOURCE_HTML = SOURCE_HTML.replace("[QUOTATION]", params.get('quotation'))
    else:
        SOURCE_HTML = SOURCE_HTML.replace("[QUOTATION]", '.')

    SOURCE_HTML = SOURCE_HTML.replace("[PAYMENT_STRUCTURE]", params.get('payment_structure'))
    SOURCE_HTML = SOURCE_HTML.replace("[QUOTATION_DATE]", params.get('quotation_date'))
    
    SOURCE_HTML = SOURCE_HTML.replace("[QTY1]", '')
    
    if params.get('desc1') != '':
        SOURCE_HTML = SOURCE_HTML.replace("[DESC1]", "<br>" + params.get('desc1'))
    else:
        SOURCE_HTML = SOURCE_HTML.replace('<td class="first-row" style="width: 800px; text-align: left; padding-left: 1em;">[DESC1]</td>', "<br><td></td>")
        
    SOURCE_HTML = SOURCE_HTML.replace("[AREA1]", params.get('area1'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL1]", get_price(params.get('price1')))

    SOURCE_HTML = SOURCE_HTML.replace("[QTY2]", '')

    if params.get('desc2') != '':
        SOURCE_HTML = SOURCE_HTML.replace("[DESC2]", params.get('desc2'))
    else:
        SOURCE_HTML = SOURCE_HTML.replace('<td style="text-align: left; padding-left: 1em;">[DESC2]</td>', "<td></td>")

    SOURCE_HTML = SOURCE_HTML.replace("[AREA2]", params.get('area2'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL2]", get_price(params.get('price2')))

    SOURCE_HTML = SOURCE_HTML.replace("[QTY3]", '')

    if params.get('desc3') != '':
        SOURCE_HTML = SOURCE_HTML.replace("[DESC3]", params.get('desc3'))
    else:
        SOURCE_HTML = SOURCE_HTML.replace('<td style="text-align: left; padding-left: 1em;">[DESC3]</td>', "<td></td>")

    SOURCE_HTML = SOURCE_HTML.replace("[AREA3]", params.get('area3'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL3]", get_price(params.get('price3')))
    
    SOURCE_HTML = SOURCE_HTML.replace("[QTY4]", '')

    if params.get('desc4') != '':
        SOURCE_HTML = SOURCE_HTML.replace("[DESC4]", params.get('desc4'))
    else:
        SOURCE_HTML = SOURCE_HTML.replace('<td style="text-align: left; padding-left: 1em;">[DESC4]</td>', "<td></td>")

    SOURCE_HTML = SOURCE_HTML.replace("[AREA4]", params.get('area4'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL4]", get_price(params.get('price4')))

    SOURCE_HTML = SOURCE_HTML.replace("[SUBTOTAL]", get_price(params.get('subtotal')))
    SOURCE_HTML = SOURCE_HTML.replace("[HST]", get_price(params.get('hst')))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL]", get_price(params.get('total')))
    
    send_to_customer = params.get('emailreport')
    recipients = []

    if send_to_customer == "1":
        recipients.append(params.get('email'))

    buf = io.BytesIO()
    pisa.CreatePDF(SOURCE_HTML, dest=buf)
    buf.seek(0)

    email_body = EMAIL_BODY.replace('[CUSTOMER_NAME]', params.get('name'))
    email_subject = f"Hi {params.get('name')}, Your Estimate is Ready!"
    email = EmailMessage(subject=email_subject, body=email_body, to=recipients, cc=['service@mastersealer.com'])
    email.content_subtype = 'html'
    email.attach(filename=f"{params.get('name')}_{params.get('address')}.pdf", content=buf.read())
    email.send()

    return SOURCE_HTML