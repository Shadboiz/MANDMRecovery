from .forms import InvoiceForm 
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .utils import generate_invoice_number, get_date_string
from email.mime.image import MIMEImage
import base64

@login_required
def invoice(request):
    invoice_form = InvoiceForm()

    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST, request.FILES)
        if invoice_form.is_valid():
            cleaned = invoice_form.cleaned_data
            request.session['customer_email'] = cleaned['email']

            # Generate Invoice Number
            invoice_number = generate_invoice_number()

            # Calculate subtotal and total
            call_out_pay = cleaned.get('call_out_pay', 0)
            roadside_pay = cleaned.get('roadside_pay', 0)
            parts_pay = cleaned.get('parts_pay', 0)
            recovery_pay = cleaned.get('recovery_pay', 0)

            sub_total = call_out_pay + roadside_pay + parts_pay + recovery_pay
            total = sub_total

            cleaned['sub_total'] = sub_total
            cleaned['total'] = total
            cleaned['invoice_date'] = get_date_string()

            # If image uploaded, prepare it for embedding
            image_cid = None
            if 'visual_damage_image' in request.FILES:
                image_file = request.FILES['visual_damage_image']
                image_cid = 'visual_damage_image'

            # Render the email HTML
            html_message = render_to_string('invoice/email_template.html', {
                'data': cleaned,
                'invoice_number': invoice_number,
                'image_cid': image_cid  # Pass the content ID
            })

            # Send using EmailMultiAlternatives
            email = EmailMultiAlternatives(
                subject=f'Invoice {invoice_number} - Your Breakdown Recovery',
                body='Please view this invoice in HTML format.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[cleaned['email']]
            )
            email.attach_alternative(html_message, "text/html")

            # Attach image if exists
            if 'visual_damage_image' in request.FILES:
                image = MIMEImage(image_file.read())
                image.add_header('Content-ID', f'<{image_cid}>')
                image.add_header('Content-Disposition', 'inline', filename=image_file.name)
                email.attach(image)

            email.send()

            return redirect('invoice_success')

    return render(request, 'invoice/invoice.html', {'invoice_form': invoice_form})

@login_required()
def invoice_success(request):
    # Get the email from session
    customer_email = request.session.get('customer_email')

    if not customer_email:
        return redirect('invoice')

    return render(request, 'invoice/success.html', {'customer_email': customer_email})
