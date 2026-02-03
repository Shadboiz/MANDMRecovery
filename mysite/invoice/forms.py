from django import forms

# Single Tailwind input class (reusable)
input_classes = "block w-full rounded-md border-gray-300 bg-white px-3 py-2 text-gray-900 placeholder-gray-400 focus:ring-indigo-600 focus:border-indigo-600 sm:text-sm"
autocomplete = "autocomplete-input"


class InvoiceForm(forms.Form):
    # --- Customer Details ---
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Customer Name", "class": input_classes}
        ),
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Address", "class": input_classes}
        ),
    )
    postcode = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Postcode", "class": input_classes}
        ),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={"placeholder": "Email Address", "class": input_classes}
        ),
    )
    telephone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Telephone", "class": input_classes}
        ),
    )

    # --- Vehicle Details ---
    vehicle = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Vehicle", "class": input_classes}
        ),
    )
    make = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Make", "class": input_classes}),
    )
    model = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Model", "class": input_classes}),
    )
    reg_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Registration Number", "class": input_classes}
        ),
    )
    load = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "Load (kg)", "class": input_classes}
        ),
    )
    caravan_trailer = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Caravan/Trailer", "class": input_classes}
        ),
    )
    colour = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Colour", "class": input_classes}),
    )
    fuel_type = forms.ChoiceField(
        required=False,
        choices=[("petrol", "Petrol"), ("diesel", "Diesel")],
        widget=forms.RadioSelect(attrs={"class": "space-x-4"}),
    )
    transmission = forms.ChoiceField(
        required=False,
        choices=[("manual", "Manual"), ("automatic", "Automatic")],
        widget=forms.RadioSelect(attrs={"class": "space-x-4"}),
    )
    keys_available = forms.ChoiceField(
        required=False,
        choices=[("yes", "Yes"), ("no", "No")],
        widget=forms.RadioSelect(attrs={"class": "space-x-4"}),
    )
    passengers = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "Number of Passengers", "class": input_classes}
        ),
    )
    other = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Other Notes", "class": input_classes}
        ),
    )

    # --- Recovery Details ---
    recovery_location = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Recovery Location", "class": input_classes}
        ),
    )
    recover_to = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Recover To", "class": input_classes}
        ),
    )
    received_by = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Received By", "class": input_classes}
        ),
    )
    arrival_time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={"type": "time", "class": input_classes}),
    )
    roadside_time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={"type": "time", "class": input_classes}),
    )
    recovery_time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={"type": "time", "class": input_classes}),
    )
    recovery_mileage = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "Recovery Mileage (mi)", "class": input_classes}
        ),
    )

    # Visual damage image upload (kept required)
    visual_damage_image = forms.ImageField(
        required=False, widget=forms.ClearableFileInput(attrs={"class": input_classes})
    )

    faults_parts_fitted = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Faults / Parts Fitted",
                "class": input_classes,
                "rows": 3,
            }
        ),
    )

    # Recovery date
    recovery_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": input_classes}),
    )

    # --- Payment details ---
    call_out_pay = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "Call Out Pay", "class": input_classes}
        ),
    )
    roadside_pay = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "Roadside Pay", "class": input_classes}
        ),
    )
    parts_pay = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "Parts Pay", "class": input_classes}
        ),
    )
    recovery_pay = forms.FloatField(
        required=False,
        widget=forms.NumberInput(
            attrs={"placeholder": "Recovery Pay", "class": input_classes}
        ),
    )
