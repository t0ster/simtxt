import { Grid } from "grommet";
import React from "react";
import { useHistory } from "react-router-dom";
import {
  Box,
  Button,
  ButtonProps,
  Flex,
  Link as RLink,
  Spinner,
  Txt,
  useTheme,
} from "rendition";

interface NavProps {
  title?: string;
  left?: React.ReactNode;
}
export function Nav({ title = "", left = null }: NavProps) {
  const theme = useTheme();
  return (
    <Grid
      columns={{ count: 3, size: "auto" }}
      gap="medium"
      pad="medium"
      style={{ backgroundColor: theme.colors.gray.main }}
    >
      {left || <Box />}
      <Txt align="center">{title}</Txt>
    </Grid>
  );
}

interface ButtonLinkProps extends ButtonProps {
  to: string;
}
export function ButtonLink({ to, ...props }: ButtonLinkProps) {
  const history = useHistory();
  return (
    <Button
      href={to}
      {...props}
      onClick={(e) => {
        e.preventDefault();
        history.push(to);
      }}
    />
  );
}

interface LinkProps {
  to: string;
  children?: React.ReactNode;
}
export function Link({ to, children = null }: LinkProps) {
  const history = useHistory();
  return (
    <RLink
      href={to}
      onClick={(e) => {
        e.preventDefault();
        history.push(to);
      }}
    >
      {children}
    </RLink>
  );
}

export function Loading({ noPadding = false }) {
  return (
    <Flex
      alignItems="center"
      justifyContent="center"
      padding={noPadding ? undefined : "20%"}
    >
      <Spinner label="Loading..." />
    </Flex>
  );
}

export function Error({ label = "Error Occured", noPadding = false }) {
  const theme = useTheme();
  return (
    <Flex
      alignItems="center"
      justifyContent="center"
      padding={noPadding ? undefined : "20%"}
    >
      <Txt color={theme.colors.danger.main}>{label}</Txt>
    </Flex>
  );
}
