import React, { useState } from 'react'
import './Book.css'


const Book = ({ id, title, authors, price }) => {
    //const dispatch = useDispatch()
    console.log(id, title, authors, price + ">>>FROM BOOK")
    const [basket, setBasket] = useState([])

    const [booktobuy, setBooktobuy] = useState({
        id: '',
        title: '',
        authors: [],
        price: ''
    })

    const saveToBasket = (e) => {
        e.preventDefault();
        if (id !== null) {
            setBooktobuy({
                id: id,
                title: title,
                authors: authors.name,
                price: price
            })
            setBasket({ ...basket, booktobuy })
            console.log("saveToBasket clicked 😝 ID is " + booktobuy.id)
            console.log(basket)
        } else {
            alert("Book was not add")
        }

    }

    return (
        <div className="book">
            <img src="https://s1.adlibris.com/images/59263007/valo-joka-ei-kadonnutkaan.jpg" alt="" />
            <div class="book__info">
                <p>Name: {title}</p>
                <p>Author: {authors.map((author) => <li>{author.name}</li>)}</p>
                <p className="book_price">Price:
                    <strong> {price}</strong>
                    <small> €</small>
                </p>
            </div>
            <button type="button" onClick={saveToBasket}>Add to Basket</button>
        </div>
    )
}

export default Book
