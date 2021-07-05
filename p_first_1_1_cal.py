#!python
print("Content-Type: text/html")
print()
import cgi

form = cgi.FieldStorage()
if "eqv_out.v_in.t" not in form or "eqv_out.v_in.s" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")
    return

t=form["eqv_out.v_in.t"].value
s=form["eqv_out.v_in.s"].value

print("속도:")

