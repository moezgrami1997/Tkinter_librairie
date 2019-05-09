def remove():
    currr = tree_book.focus()
    Ll=tree_book.item(currr)
    cinn=Ll['values'][2]
    role = Ll['values'][3]
    if(role==1):
        c.execute("""Update User SET role=? WHERE cin=?""",(0,cinn))
    elif(role==2):
        c.execute("""Update User SET role=? WHERE cin=?""",(1,cinn))
    conn.commit()