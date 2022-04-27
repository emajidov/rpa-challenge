import xlsxwriter
from dateutil.relativedelta import relativedelta
from datetime import date


def build_start_date(months):
    now = date.today()
    start = now - relativedelta(months=months)
    return f"{start.month:02d}/01/{start.year}"


def contains_money_amount(title, description):
    currency = ['$', 'USD', 'dollars']
    return any(i in description for i in currency) or any(i in title for i in currency)


def count_search_term(title, description, term):
    return title.count(term) + description.count(term)


def write_to_excel(title, date, description, image_filename, amount_of_phrases, contains_money=False):
    workbook = xlsxwriter.Workbook("result.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Title")
    worksheet.write(1, 0, title)

    worksheet.write(0, 1, "Description")
    worksheet.write(1, 1, description)

    worksheet.write(0, 2, "Date")
    worksheet.write(1, 2, date)

    worksheet.write(0, 3, "Image Filename")
    worksheet.write(1, 3, image_filename)

    worksheet.write(0, 4, "Amount of search phrases")
    worksheet.write(1, 4, amount_of_phrases)

    worksheet.write(0, 5, "Contains Money Amount")
    worksheet.write(1, 5, contains_money)

    workbook.close()
