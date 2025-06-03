#cond true
True

#cond false
False

#cond
if True:
    print("block IF be executed")
else:
    print("block ELSE don't be executed")

#operator logic: 'and' & 'or'
if True and True:
    print("block be executed")

if True and False:
    print("block don't be executed")

if False and False:
    print("block don't be executed")

# OR
if True or False:
    print("block be executed")

if False or False:
    print("block don't be executed")

if True or True:
    print("block be executed")