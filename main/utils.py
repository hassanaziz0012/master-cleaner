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
        <title>MasterCleaner Report</title>

        <!-- Bootstrap CSS -->
        <style>
            .logo img {
                width: 240px;
                height: 55px;
            }

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

        </style>
    </head>

    <body class="container">
        <div class="logo">
            <img src="https://i.imgur.com/BT6GFNC.jpg" alt="Logo">
        </div>
        <div class="header">
            <h2 style="font-size: 16px; line-height: 0.1px; margin: 0; padding: 10px 0;">PROPERTY SERVICES!</h2>
            <h2 style="font-size: 16px; line-height: 0.1px; margin: 0; padding: 10px 0;">CELEBRATING 25 YEARS!</h2>
        </div>

        <br>
        <div class="contact-info" style="font-size: 12px;">
            <h4>TOLL-FREE: 1-855-SEALED-0</h4>
            <h4>905 Region: 905-850-8955</h4>
            <h4>416 Region: 416-450-1157</h4>
            <h4>service@mastersealer.com</h4>
            <h4>www.mastersealer.com</h4>
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
                        <th>DESCRIPTION OF SERVICES</th>
                        <th class="area-header">AREA</th>
                        <th class="total-header">TOTAL</th>
                    </thead>
                    <tbody>
                        <tr class="service-row">
                            <td class="quantity-cell first-row">[QTY1]</td>
                            <td class="first-row">[DESC1]</td>
                            <td class="first-row">[AREA1]</td>
                            <td class="first-row" style="border-right: 1px solid lightgray;">[TOTAL1]</td>
                        </tr>

                        <tr class="service-row">
                            <td class="quantity-cell">[QTY2]</td>
                            <td>[DESC2]</td>
                            <td>[AREA2]</td>
                            <td style="border-right: 1px solid lightgray;">[TOTAL2]</td>
                        </tr>

                        <tr class="service-row">
                            <td class="quantity-cell">[QTY3]</td>
                            <td>[DESC3]</td>
                            <td>[AREA3]</td>
                            <td style="border-right: 1px solid lightgray;">[TOTAL3]</td>
                        </tr>

                        <tr class="border-bottom-row service-row">
                            <td class="quantity-cell">[QTY4]</td>
                            <td>[DESC4]</td>
                            <td>[AREA4]</td>
                            <td style="border-right: 1px solid lightgray;">[TOTAL4]</td>
                        </tr>

                        <!-- TOTALS -->
                        <tr class="padding-top-row">
                            <td class="no-border"></td>
                            <td class="no-border"></td>
                            <td class="bg-success text-white no-border"><b>Subtotal</b></td>
                            <td class="bg-success text-white border-row">[SUBTOTAL]</td>
                        </tr>

                        <tr class="padding-top-row">
                            <td class="no-border"></td>
                            <td class="no-border"></td>
                            <td class="bg-success text-white no-border"><b>HST</b></td>
                            <td class="bg-success text-white border-row">[HST]</td>
                        </tr>

                        <tr class="padding-top-row">
                            <td class="no-border"></td>
                            <td class="no-border"></td>
                            <td class="bg-success text-white no-border"><b>Total</b></td>
                            <td class="bg-success text-white border-row">[TOTAL]</td>
                        </tr>

                    </tbody>
                </table>
            </div>

            <div class="credit">
                <p>Quotation prepared by: <span class="underline">[ESTIMATOR]</span></p>
                <p>If you would like to accept this quotation or if you have any questions, please call or email:
                    905-850-8955 - Service@mastersealer.com</p>

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
    SOURCE_HTML = SOURCE_HTML.replace("[DESC1]", "<br>" + params.get('desc1'))
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
    
    print(params.get('desc4'))
    SOURCE_HTML = SOURCE_HTML.replace("[QTY4]", '')
    SOURCE_HTML = SOURCE_HTML.replace("[DESC4]", params.get('desc4'))
    SOURCE_HTML = SOURCE_HTML.replace("[AREA4]", params.get('area4'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL4]", params.get('price4'))
    print(params.get('desc4'))

    SOURCE_HTML = SOURCE_HTML.replace("[SUBTOTAL]", params.get('subtotal'))
    SOURCE_HTML = SOURCE_HTML.replace("[HST]", params.get('hst'))
    SOURCE_HTML = SOURCE_HTML.replace("[TOTAL]", params.get('total'))
    
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