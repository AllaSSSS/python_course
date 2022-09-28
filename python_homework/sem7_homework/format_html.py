def write(filename, book):
    with open (filename + '.html', 'w') as file:
        file.write('<html><body><table>')
        for rec in book:
            last_name, first_name, phone = rec 
            file.write(f'<tr><td>{last_name}</td><td>{first_name}</td><td>{phone}</td></tr>')
        file.write('</table></body></html>')