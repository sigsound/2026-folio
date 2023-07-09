import * as React from "react"
import { Link } from "gatsby"
import styled from 'styled-components'

const TitleGroup = styled.div`
    height: 310px;
    opacity: 0;
    background-color: #F5F5F5;
    border-radius: 0;
    justify-content: center;
    align-items: center;
    margin: 20px;
    padding: 20px;
    display: block;
    position: relative;
    bottom: 0;
    left: 0;
    right: 0;
    transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
`
const CardStyle = styled.div`
    background-image: url(${props => props.image});
    background-size: cover;
    width: 100%;
    height: 390px;
    position: relative;
    overflow: hidden;
    display: grid;
    grid-template-rows: 1fr 1fr;
`

const Title = styled.h3`
    color: #171717;
    font-size: 24px;
    line-height: 1.8;
    margin: 0;
`

const Credits = styled.p`
    color: #333333;
    font-weight: 600;
    font-size: 14px;
    line-height: 1.3;
    align-self: end;
`

const Cards = styled.div`
    border: 1px solid #27FFCB;
    .CardLink {
        @media (min-width: 768px) {
          :hover ${TitleGroup} {
            opacity: 1;
          }
    }
`

const Card = ({ title, credits, image, contentfulId }) => (
  <Cards>
    <Link to={`/case-studies/${contentfulId}`} className="CardLink">
      <CardStyle image={image}>
        <TitleGroup>
          <Title>{title}</Title>
          <Credits>{credits}</Credits>
        </TitleGroup>
      </CardStyle>
    </Link>
  </Cards>
)

export default Card
