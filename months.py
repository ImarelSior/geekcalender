from datetime import date
import calendar
def table(month,year):
    first_day = date(year,month,1)
    lest_day = date(year,month,calendar.monthrange(year,month)[1])
    x = first_day.weekday()+1 if first_day.weekday()!=6 else 0
    print('<table>')
    print('''\t<tr>
        <td> יום ראשון</td>
        <td> יום שני</td>
        <td> יום שלישי</td>
        <td> יום רביעי</td>
        <td> יום חמישי</td>
        <td> יום שישי</td>
        <td> יום שבת</td>
    </tr>''')
    print('\t<tr>')
    while x:
        print('\t\t<td></td>')
        x = x-1
    for day in range(lest_day.day):
        my_date = date(year,month,day+1)
        print(f'\t\t<td>{day+1}</td>')
        if my_date.weekday() == 5:
            print('''\t</tr>
    <tr>''')
    x = 5-lest_day.weekday()
    while x>0:
        print('\t\t<td></td>')
        x = x-1
    print('''\t</tr>
</table>''')
table(6,2024)