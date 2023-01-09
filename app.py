from flask import render_template, request
import config
import rates 

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        entry_date = request.form.get('rate_date')
        entry_amount = request.form.get('amount')
        entry_base_ccy = request.form.get('base_currency')
        entry_quote_ccy = request.form.get('quote_currency')

        base_dict = rates.read_one(entry_date, entry_base_ccy)
        quote_dict = rates.read_one(entry_date, entry_quote_ccy)
        rate = quote_dict['rate'] / base_dict['rate']
        output_amount = round(float(entry_amount) * rate, 2)

        conversion_info = {
            'entry_date': entry_date,
            'entry_amount': entry_amount, 
            'entry_base_ccy': entry_base_ccy, 
            'entry_quote_ccy': entry_quote_ccy, 
            'rate': rate, 
            'output_amount': output_amount
        }
    
        return render_template('home.html', conversion_info=conversion_info)

    else: 
        # some defaults
        conversion_info = {
            'entry_date': '2022-01-01',
            'entry_amount': '100', 
            'entry_base_ccy': 'USD', 
            'entry_quote_ccy': 'EUR', 
            'rate': '', 
            'output_amount': ''
        }

        return render_template('home.html', conversion_info=conversion_info)



if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8000, debug=True)
