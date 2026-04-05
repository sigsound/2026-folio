import { defineCollection, z } from 'astro:content';

const projects = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    role: z.string(),
    timeline: z.string(),
    impact: z.string(),
    thumbnail: z.string(),
    hero: z.string(),
    hisImage: z.string(),
    video1: z.string().optional(),
    video2: z.string().optional(),
    media: z.array(z.object({
      src: z.string(),
      alt: z.string()
    })).optional()
  }),
});

const about = defineCollection({
  type: 'content',
  schema: z.object({
    headline: z.string(),
    profileImage: z.string()
  }),
});

export const collections = { projects, about };