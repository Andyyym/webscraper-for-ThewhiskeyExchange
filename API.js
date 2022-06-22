const PORT = 8000
const redwine = require('./data.json')
const express = require('express')

const app = express()

app.get('/',(req,res) =>{
    res.json('welcome to wine api')
})

app.get('/red', (req,res) => {

    res.json(redwine)

})

app.listen(PORT, () => console.log(`server is running on PORT ${PORT}`))





