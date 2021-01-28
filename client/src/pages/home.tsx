import { gql, useMutation, useQuery } from "@apollo/client";
import { Error, Link, Loading, Nav } from "components";
import { Grid } from "grommet";
import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { Button, Flex, Textarea } from "rendition";
import styled from "styled-components";
import * as Type from "types";

const StyledText = styled(Flex)`
  border-bottom: solid 1px rgba(0, 0, 0, 0.33);
  height: 72px;
  align-items: center;
`;

function trim(text: string) {
  if (text.length > 206) {
    return text.replace(/^(.{200}[^\s]*).*/s, "$1 [...]");
  }
  return text;
}

const GET_TEXTS = gql`
  query GetTexts {
    texts {
      id
      content
    }
  }
`;
function Texts() {
  const { data, loading, error } = useQuery<{ texts: Type.Text[] }>(GET_TEXTS, {
    returnPartialData: true,
  });

  if (loading) {
    return <Loading />;
  }
  if (error) {
    return <Error label={error.toString()} />;
  }

  return (
    <Grid align="center">
      {data?.texts?.map((txt) => (
        <Link key={txt.id} to={`/text/${txt.id}`}>
          <StyledText>{trim(txt.content)}</StyledText>
        </Link>
      ))}
    </Grid>
  );
}

const CREATE_TEXT = gql`
  mutation createText($content: String!) {
    createText(content: $content) {
      id
      content
    }
  }
`;
function AddText() {
  const [content, setContent] = useState("");
  const history = useHistory();
  const [createText] = useMutation<
    { createText: Type.Text },
    { content: string }
  >(CREATE_TEXT, {
    // @ts-ignore
    update(cache, { data: { createText } }) {
      cache.modify({
        fields: {
          texts(existingTexts = []) {
            const newTextRef = cache.writeFragment({
              // eslint-disable-next-line
              data: createText,
              fragment: gql`
                fragment NewText on Text {
                  id
                  content
                }
              `,
            });
            // eslint-disable-next-line
            return [newTextRef, ...existingTexts];
          },
        },
      });
    },
    // TODO: This causes `Can't perform a React state update on an unmounted component.` warning
    onCompleted({ createText }) {
      history.push(`/text/${createText.id}`);
    },
  });
  return (
    <>
      <Textarea value={content} onChange={(e) => setContent(e.target.value)} />
      <Button
        primary
        disabled={!content}
        onClick={(e) => {
          createText({ variables: { content } });
          setContent("");
        }}
      >
        Add Text
      </Button>
    </>
  );
}
export default function Home() {
  return (
    <>
      <Nav title="All Texts" />
      <Grid gap="medium" pad="large">
        <AddText />
        <Texts />
      </Grid>
    </>
  );
}
