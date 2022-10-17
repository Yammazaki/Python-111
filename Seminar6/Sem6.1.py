doc = input().split()
print(doc)
# 2 + 3 * 2 - 1 + 4 / 2
while ('*' in doc) or ('/' in doc):
    mult_ind = -1
    div_ind = -1
    if '*' in doc:
        mult_ind = doc.index('*')
    if '/' in doc:
        div_ind = doc.index('/')
        
    if (mult_ind < div_ind) and (mult_ind != -1):
        doc = doc[:mult_ind - 1] + [float(doc[mult_ind - 1]) * float(doc[mult_ind + 1])] + doc[mult_ind + 2:]
    else:
        doc = doc[:div_ind - 1] + [float(doc[div_ind - 1]) / float(doc[div_ind + 1])] + doc[div_ind + 2:]
        
while ('+' in doc) or ('-' in doc):
    sum_ind = -1
    dif_ind = -1
    if '+' in doc:
        sum_ind = doc.index('+')
    if '-' in doc:
        dif_ind = doc.index('-')
        
    if (sum_ind < dif_ind) and (sum_ind != -1):
        doc = doc[:sum_ind - 1] + [float(doc[sum_ind - 1]) + float(doc[sum_ind + 1])] + doc[sum_ind + 2:]
    else:
        doc = doc[:dif_ind - 1] + [float(doc[dif_ind - 1]) - float(doc[dif_ind + 1])] + doc[dif_ind + 2:]
    
print(doc)



