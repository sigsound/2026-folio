import * as React from "react"
import { graphql } from "gatsby"
import { renderRichText } from "gatsby-source-contentful/rich-text"

import Seo from "../components/seo"
import Layout from "../components/layout"
import Card from "../components/card"

const IndexPage = ({ data }) => {
  const projects = data?.allContentfulCaseStudy?.edges || []
  const about = data?.allContentfulAbout?.edges || []

  // Check if about data is available
  const aboutData = about.length > 0 ? about[0].node : null

  return (
    <Layout>
      <div className="Hero">
        <div className="HeroGroup">
          <h1>Nick Woods is a Lead Product Designer based in the Bay Area</h1>
        </div>
      </div>

      <div className="Cards two-col">
        {projects.map(({ node }) => (
          <Card
            key={node.contentful_id}
            title={node?.title || null}
            credits={node?.credits || null}
            image={node?.projectThumb?.file?.url || null}
            contentfulId={node.contentful_id}
          />
        ))}
      </div>

      <div className="about">

        {aboutData && (
          <img
            src={aboutData.profileImage.file.url}
            alt={aboutData.profileImage.description}
          />
        )}

        <div className="about-text">
        <h1>{aboutData?.headline}</h1>
        <div>{renderRichText(aboutData?.detail)}</div>
        </div>

      </div>

      <div className="skills"></div>
    </Layout>
  )
}

export const query = graphql`
  query {
    allContentfulCaseStudy {
      edges {
        node {
          contentful_id
          title
          credits
          projectThumb {
            file {
              url
            }
          }
        }
      }
    }
    allContentfulAbout {
      edges {
        node {
          profileImage {
            file {
              url
            }
            description
          }
          headline
          detail {
            raw
          }
        }
      }
    }
  }
`

export const Head = () => <Seo title="Home" />

export default IndexPage
