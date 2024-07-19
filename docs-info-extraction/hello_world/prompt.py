def get_system_prompt():
    system_prompt = """
You are an office assistant and work analyzing the content of invoices
"""
    return system_prompt


def get_user_prompt():

    json_response_format = """
<json>
{
    "Create_date_time":
    "client_name":
    "net_amount":
    "taxes":
    "due_date":
    "document_number"
    "Discount"
}
</>json
"""
    user_prompt = f"""
Your task is to extract the following information from the document that was sent:

<info>
    - Create Date and Time
    - Client's Name/Company Name
    - Net Amount of the Invoice
    - Taxes
    - Payment Code of the Boleto
    - Due Date
    - Document Number
    - DISCOUNT
</info>

    Take a deep breath and carefully review your response. Make sure to check the formatting and information of the JSON several times to ensure there are no errors.
    Your response is crucial to the process, so pay close attention to the accuracy of the JSON formatting.
    The response format should follow:
    {json_response_format}
"""
    return user_prompt
