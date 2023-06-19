from flask import Flask,render_template,request,session
import random


app = Flask(__name__)
app.secret_key = '1234'

# ( )
# print ( )

@app.route('/')
def home( ):
    return render_template('home.html')



@app.route('/over',methods=['GET',"POST"])
def over( ):
    if request.method == "POST":
        
        run = int (request.form['run'])
        bowl = random.randint(1,6) # change back


        # Wicket Check
        if (run != bowl):
            target = runcal(run,bowl)
        else:
            target = wicket()

            return render_template('summary.html',target=target)

        # Result Check
        
        if (target['bal']==0) or (target['check']=='stop'):
            return render_template('summary.html',target=target)
        return render_template('over.html',target=target)


    session.clear()
    target = initial( )        
    return render_template('over.html',target = target)
    



def initial( ):
    bal = 6
    tar = int( random.randint(15,36))
    score = 0
    run = ''
    rr = 0
    req = tar/bal
    msg=''
    bowl =''
    check='continue'
    last = ''

    session['tar']   = tar
    session['bal']   = bal
    session['score'] = score
    session['last']  = last

    result = {'tar':tar , 'run':run, 'bal': bal , 'rr':round(rr,2) , 'req':round(req,2) ,'score':score,'msg':msg ,'bowl':bowl , 'check':check,'last':last}
    return result

# round(rr,2) 
# round(req,2)

# tar,run,bal
def runcal(run,bowl):
    tb    = 6
    tar   = session['tar']
    run   = run
    bowl  = bowl
    bal   = session['bal']
    score = session['score']
    last  = session['last']

    last  = last + str(run)
    score = score + run
    bal   = bal -1

    try:
        req = ( (tar - score )/bal)
        rr  =  (score / ( tb+(bal+1) ))

    except ZeroDivisionError:
        req =  ( (tar )/tb)
        rr  =  (score /tb)
    

    if ((tar>score) & (bal>0)): 
        msg   = 'Keep Rocking'
        check = 'continue'
    
    elif ((tar>score) & (bal==0)): 
        msg   = 'You lose the game'
        check = 'stop'
    
    elif ((score>=tar) & (bal>0)): 
        msg   = 'You Won the game'
        check = 'stop'
    
    elif ((score>=tar) & (bal==0)): 
        msg   = 'You Won the game'
        check = 'stop'
    
    else: 
        msg   = 'Technical Issue'
        check = 'stop'

    

    session['score'] = score
    session['bal']   = bal
    session['last']  = last

    result = {'tar':tar , 'run':run , 'bal': bal , 'rr':round(rr,2) , 'req':round(req,2),'score':score,'msg':msg,'bowl':bowl,'check':check,'last':last}

    return result



def wicket():
    run = "Wicket"
    tar   = session['tar']
    bal   = session['bal'] - 1
    score = session['score']
    last  = session['last']
    last  = last + run
    msg   = 'You lose the game'
    check = ''   
    bowl  = ''
    result = {'tar':tar , 'run':run , 'bal': bal , 'rr':'' , 'req':'','score':score,'msg':msg,'bowl':bowl,'check':check,'last':last}

    return result




















if __name__ == '__main__':
    app.run(debug=True)

