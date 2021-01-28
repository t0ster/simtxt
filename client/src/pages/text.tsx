import { gql, useQuery } from "@apollo/client";
import { ButtonLink, Error, Link, Loading, Nav } from "components";
import React, { useEffect, useMemo } from "react";
import { IoChevronBackCircle } from "react-icons/io5";
import { useParams } from "react-router-dom";
import { Accordion, Table } from "rendition";
import * as Type from "types";

const GET_SENTENCE = gql`
  query GetSentence($id: ID!) {
    sentence(id: $id) {
      content
      similar {
        sentence {
          content
          textId
        }
        score
      }
    }
  }
`;
interface SimilarProps {
  sentenceId: string;
}
function Similar({ sentenceId }: SimilarProps) {
  const { data, loading, error, startPolling, stopPolling } = useQuery<{
    sentence: Type.Sentence;
  }>(GET_SENTENCE, {
    variables: { id: sentenceId },
    fetchPolicy: "cache-and-network",
  });
  useEffect(() => {
    startPolling(5000);
    return () => {
      stopPolling();
    };
  }, [startPolling, stopPolling]);
  if (loading) {
    return <Loading noPadding />;
  }
  if (error) {
    return <Error label={error.toString()} />;
  }
  return (
    <Table
      columns={[
        {
          field: "Sentence",
        },
        {
          field: "Score",
          sortable: true,
        },
        {
          field: "Text",
        },
      ]}
      data={data?.sentence.similar.map((sim) => ({
        Sentence: sim.sentence.content,
        Score: sim.score.toFixed(4),
        Text: (
          <Link to={`/text/${sim.sentence.textId}`}>
            {sim.sentence.textId.substr(0, 8)}
          </Link>
        ),
      }))}
    />
  );
}

const GET_TEXT = gql`
  query GetText($id: ID!) {
    text(id: $id) {
      sentences {
        id
        content
      }
    }
  }
`;
function Sentences() {
  const { id } = useParams<{ id: string }>();
  const { data, loading, error, startPolling, stopPolling } = useQuery<{
    text: Type.Text;
  }>(GET_TEXT, {
    variables: { id },
  });
  const sentences = useMemo(() => data?.text?.sentences || [], [data]);
  useEffect(() => {
    if (sentences.length === 0) {
      startPolling(500);
    } else {
      stopPolling();
    }
  }, [sentences, startPolling, stopPolling]);

  if (loading || sentences.length === 0) {
    return <Loading />;
  }
  if (error) {
    return <Error label={error.toString()} />;
  }
  return (
    <Accordion
      key={id}
      // @ts-ignore
      items={sentences.map((sentence) => ({
        label: sentence.content,
        panel: <Similar sentenceId={sentence.id} />,
      }))}
    />
  );
}

export default function Text() {
  const { id }: { id: string } = useParams();
  return (
    <>
      <Nav
        left={
          <ButtonLink
            plain
            width={24}
            icon={<IoChevronBackCircle size={24} />}
            to="/"
          />
        }
        title={`Text # ${id.substr(0, 8)}`}
      />
      <Sentences />
    </>
  );
}
