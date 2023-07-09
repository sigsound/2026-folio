import React from "react"
import { graphql } from "gatsby"
import { renderRichText } from "gatsby-source-contentful/rich-text"
import Layout from "../components/layout"

const CaseStudyTemplate = ({ data }) => {
  const {
    credits,
    framing,
    projectHero,
    projectContent,
    media,
  } = data.contentfulCaseStudy

  return (
    <Layout>

    <div className="cs-hero">
        <div className="cs-hero-group"><h1>{renderRichText(framing)}</h1></div>
    </div>

    <div className="cs-content">
      <p>{credits}</p>
      <img src={projectHero.file.url} alt="" />
      <div>{renderRichText(projectContent)}</div>
      {media.map((media, index) => (
      <img key={index} src={media.file.url} alt="" />
      ))}
    </div>

    </Layout>
  )
}

export const query = graphql`
  query($contentful_id: String!) {
    contentfulCaseStudy(contentful_id: { eq: $contentful_id }) {
      contentful_id
      credits
      creationDate
      framing {
        raw
      }
      projectHero {
        file {
          url
        }
      }
      projectContent {
        raw
      }
      media {
        file {
          url
        }
      }
    }
  }
`

export default CaseStudyTemplate