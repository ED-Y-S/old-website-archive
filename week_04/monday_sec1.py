def delete_HTML(text):
    '''
    This function removes all HTML tags from the input text.

    >>> delete_HTML('This is <b>bold</b>!')
    'This is bold!'
    >>> delete_HTML('This is <i>italic</i>!')
    'This is italic!'
    >>> delete_HTML('This is <strong>italic</strong> and this is <ins>strikethrough</ins>!')
    'This is italic and this is strikethrough!'
    '''
    '''
    text = text.replace('<b>', '')
    text = text.replace('</b>', '')
    text = text.replace('<i>', '')
    text = text.replace('</i>', '')
    '''
    # .replace is only good if there's and specific string that you want to replace; it doesnt work in pattern
    new_text= ''
    inside_tag = False #True whenever it's in the greater-than and smaller-than
    for i in range(len(text)):
        if text[i]=='<':
            inside_tag = True
        elif text[i] == '>':
            inside_tag = False
        elif inside_tag == False:
            new_text += text[i]
    return new_text

    '''
next_text = ''
lessthans= text.split('<')
for lessthan in lessthans
    '''