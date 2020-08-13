from django.test import TestCase

# Create your tests here.
query_rate = []


def rates_voice():
    global query_rate
    if len(query_rate) == 0:
        play_query('request_postal_code_text.mp3')
        request_postal_code_text = record()
        query_rate.append(request_postal_code_text)
        return

    if len(query_rate) == 1:
        play_query('reciepent_postal_code_text.mp3')
        reciepent_postal_code_text = record()
        query_rate.append(reciepent_postal_code_text)
        return

    if len(query_rate) == 2:
        play_query('weight_text.mp3')
        weight_text = record()
        query_rate.append(weight_text)
        return

    if len(query_rate) == 3:
        rate = check_rates(query_rate[0], query_rate[1], query_rate[2])
        message_out = "The rate for delivering a " + str(query_rate[2]) + " pounds package from " + str(
            query_rate[0]) + "to " + str(query_rate[1]) + " is " + str(rate) + " Dollors"
        texttovoice(message_out, 'filename')

        return query_rate, rate, message_out