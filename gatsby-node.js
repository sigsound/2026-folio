/**
 * Implement Gatsby's Node APIs in this file.
 *
 * See: https://www.gatsbyjs.com/docs/reference/config-files/gatsby-node/
 */

/**
 * @type {import('gatsby').GatsbyNode['createPages']}
 */
exports.createPages = async ({ actions, graphql }) => {
  const { createPage } = actions

  const result = await graphql(`
    query {
      allContentfulCaseStudy {
        edges {
          node {
            contentful_id
          }
        }
      }
    }
  `)

  if (result.errors) {
    throw new Error("Error retrieving case studies from Contentful:", result.errors)
  }

  const caseStudies = result.data.allContentfulCaseStudy.edges

  caseStudies.forEach(({ node }) => {
    createPage({
      path: `/case-studies/${node.contentful_id}`,
      component: require.resolve("./src/templates/case-study.js"),
      context: {
        contentful_id: node.contentful_id,
      },
    })
  })
}



