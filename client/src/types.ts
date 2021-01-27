export interface Sentence {
  id: string;
  content: string;
  textId: string;
  similar: [Similar];
}

export interface Similar {
  sentence: Sentence;
  score: number;
}

export interface Text {
  id: string;
  content: string;
  sentences: Sentence[];
}
