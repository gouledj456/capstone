import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import './productSearch.css';
import Box from '@mui/material/Box';
import { useEffect, useState, useMemo } from 'react';
import axios from 'axios';

// frontend / src / components / products / ViewEditProduct.js

import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Slide from '@mui/material/Slide';
import Input from '@mui/material/Input';
import InputLabel from '@mui/material/InputLabel';
import Checkbox from '@mui/material/Checkbox';


import useDebounce from '../hooks/use-debounce.js';



// frontend / src / components / products / AddProduct.js

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="down" ref={ref} {...props} />;
});

const ariaLabel = { 'aria-label': 'description' };

const url = "http://127.0.0.1:8000/api"


//Search bar functionality will handle search but also items that come up below, don't make another component for it.
//Have an onlick function thats calls another function, and that function sets the state of the props and calls it to another function
export default function CustomerProductPage() {
  const [products, setProducts] = useState([]);
  const [load, setLoad] = useState(false);
  const [productClick, setproductClick] = useState(false);
  const [searchQuery, setsearchQuery] = useState("")

  //OnClick product view

  const [open, setOpen] = React.useState(false);
  const [productName, setproductName] = useState(null);
  const [productDescription, setproductDescription] = useState(null);
  const [productQuantity, setproductQuantity] = useState(null);
  const [productPrice, setproductPrice] = useState(null);
  const [productPriceSale, setproductPriceSale] = useState(null);
  const [productWeight, setproductWeight] = useState(null);
  const [productHeight, setproductHeight] = useState(null);



  const [productClickedInfo, setproductClickedInfo] = useState({});

  const [EditInputLabels, setEditInputLabels] = useState(false)

  const [buttonClicked, setButtonClicked] = useState(false);

  const debounce = useDebounce(searchQuery, 500)

  const [selectedCategory, setSelectedCategory] = useState();




  useEffect(() => {
    fetchData()

  }, [debounce])


  const fetchData = async () => {

    const endpoint = `${url}/Products?product_name=${searchQuery}`

    axios.get(endpoint)
      .then((response) => {
        setProducts(response.data);
        setLoad(true);

      })
  }

  console.log(products)

  const handleClickOpen = () => {
    setOpen(true);
  };

  const exitProductAdd = () => {
    setOpen(false);
    setproductClick(false);
  }

  //when product is clicked
  const editFields = () => {
    setButtonClicked(true);
    setEditInputLabels(true);
    console.log("PRESS")

  };

  const handleClose = () => {

    setButtonClicked(false);
    setEditInputLabels(false);
    setOpen(false);
  };



  const updateProductInfo = () => {
    if (buttonClicked) {
      const updatedProduct = {
        product_id: productClickedInfo.productId,
        product_name: productClickedInfo.productName,
        product_description: productClickedInfo.productDescription,
        product_quantity: productClickedInfo.productQuantity,
        product_price: productClickedInfo.productPrice,
        product_price_sale: productClickedInfo.productPriceSale,
        product_weight: productClickedInfo.productWeight,
        product_height: productClickedInfo.productHeight,
        image: productClickedInfo.image
      };

      let form_data = new FormData();


      form_data.append('product_name', productName);
      form_data.append('product_description', productDescription);
      form_data.append('product_quantity', productQuantity);
      form_data.append('product_price', productPrice);
      form_data.append('product_height', productHeight);
      form_data.append('product_price_sale', 0)
      form_data.append('product_weight', productWeight);
      // form_data.append('image', fileurl, fileurl.name);

      console.log(updatedProduct)

      axios
        .put(`http://127.0.0.1:8000/api/Products/${updatedProduct.product_id}/`, form_data, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then((response) => {
          console.log(response);
          const updatedProducts = [...products];
          const index = updatedProducts.findIndex((product) => product.id === productClickedInfo.id);
          updatedProducts[index] = response.data;
          setProducts(updatedProducts);
        })
        .catch((error) => {
          console.log(error);
        });
    }

    setButtonClicked(false);
    setEditInputLabels(false);
    setOpen(false);
  }

  const signInDiv = document.getElementById('signInDiv');
  if (signInDiv) {
    signInDiv.hidden = true;
  }

  const showproductClick = (productClicked) => {
    const selectedProduct = products[productClicked];
    console.log("SELECTED PRODUCT")
    console.log(selectedProduct)
    const imageShortenUrl = selectedProduct.image.substring(selectedProduct.image.lastIndexOf('/') + 1)

    setproductName(selectedProduct.product_name)
    setproductPrice(selectedProduct.product_price)
    setproductHeight(selectedProduct.product_height)
    setproductWeight(selectedProduct.product_weight)
    setproductQuantity(selectedProduct.product_quantity)
    setproductDescription(selectedProduct.product_description)

    setproductClickedInfo({
      productId: selectedProduct.product_id,
      productName: selectedProduct.product_name,
      productDescription: selectedProduct.product_description,
      productQuantity: selectedProduct.product_quantity,
      productPrice: selectedProduct.product_price,
      productPriceSale: selectedProduct.product_price_sale,
      productWeight: selectedProduct.product_weight,
      productHeight: selectedProduct.product_height,
      productImage: imageShortenUrl
    });
    console.log(imageShortenUrl)
    setOpen(true);

    // console.log(products[productClicked]);

  }



  // console.log(products)
  return (
    <div className="item-gallery-box">
      <div className="search-bar">
        <input
          type='search'
          placeholder="search.."
          value={searchQuery}
          onChange={e => setsearchQuery(e.target.value)}
        />


      </div>
      <div class="straight-line"></div>

      <div className='item-flex'>
        {products && products.map((item, id) => (
          <div onClick={() => showproductClick(id)} key={id} className="product-details-list">
            <div className="product-name">{item.product_name}</div>
            {/* <div className="product-description"> {item.product_description}</div> */}
            <img className="product-img" src={require('/src/productimages/' + item.image.substring(item.image.lastIndexOf('/') + 1))} />
            <div className="product-price-map">{"$ " + item.product_price.toFixed(2)}</div>
            <div className="product-avaliable">{"Quantity: " + item.product_quantity}</div>

            {/* <div className="product-ships">{item.product_height}</div> */}
            {/* <div className="product-avaliable">{item.product_available === "false" ? "true" : "Avaliable "}</div> */}
            {/* background: #D9D9D9;
mix-blend-mode: overlay;
border-radius: 12px; */}
            <Button variant="contained" color="primary" size="large" style={{ padding: '3px 10px', background: '#D9D9D9', mixBlendMode: 'overlay', marginTop: '1rem', color: 'black' }}>
              Buy Now
            </Button>
          </div>
        ))}


      </div>

      <Dialog className='product-click-window' open={open} onClose={handleClose}>
        <DialogContent>
          {productClickedInfo.productImage ? (
            <img className="product-clicked-img" src={require('/src/productimages/' + productClickedInfo?.productImage)} />
          ) : null}


          <div className="product-details">
            {/* product Name placeholder */}
            <div className="product-name-tag">
              <h4 className="product-name">Product Name:</h4>
              <Input onChange={e => setproductName(e.target.value)} disabled={!EditInputLabels} fullWidth={true} disableUnderline={true} placeholder="Product Name" label="Test" defaultValue={productClickedInfo.productName} />
            </div>

            {/* product price placeholder */}
            <div className="product-price-tag">
              <h4 className="product-price">Product Price:</h4>
              <Input onChange={e => setproductPrice(e.target.value)} disabled={!EditInputLabels} fullWidth={true} disableUnderline={true} placeholder="Price" defaultValue={productClickedInfo.productPrice + "$"} />
            </div>

            <div className="product-dimensions-tag">
              <h4 className="product-dimensions">Product Dimensions:</h4>
              <Input onChange={e => setproductHeight(e.target.value)} disabled={!EditInputLabels} fullWidth={true} disableUnderline={true} placeholder="Dimensions" defaultValue={productClickedInfo.productHeight + "x" + productClickedInfo.productWidth} />
            </div>

            <div className="product-weight-tag">
              <h4 className="product-weight">Product Weight</h4>
              <Input onChange={e => setproductWeight(e.target.value)} disabled={!EditInputLabels} fullWidth={true} disableUnderline={true} placeholder="Weight" defaultValue={productClickedInfo.productWeight + 'kg'} />
            </div>

            <div className="product-quantity-tag">
              <h4 className="product-quantity">Product Quantity</h4>
              <Input onChange={e => setproductQuantity(e.target.value)} disabled={!EditInputLabels} fullWidth={true} disableUnderline={true} placeholder="Quantity" defaultValue={productClickedInfo.productQuantity} />
            </div>


          </div>


          <h3 className="product-description-title">Product Description</h3>
          <Input onChange={e => setproductDescription(e.target.value)} disabled={!EditInputLabels} disableUnderline={true} multiline={true} placeholder="Product Description" defaultValue={productClickedInfo.productDescription} inputProps={ariaLabel} />
        </DialogContent>
        <DialogActions>
          {/* <Button onClick={handleClose}>
            {buttonClicked ? "Changes Made" : "Make Changes"}
          </Button> */}
          {/* {buttonClicked ? "Changes Made" : "Make Changes"} */}
          {buttonClicked ? (
            <Button onClick={updateProductInfo} className="confirm-changes-button">Confirm Changes</Button>
          ) : null}
          <Button className="edit-window-button" variant="contained" onClick={editFields}>

            {buttonClicked ? "" : "Edit Product Info"}
          </Button>




        </DialogActions>
      </Dialog>
    </div >
  )
}