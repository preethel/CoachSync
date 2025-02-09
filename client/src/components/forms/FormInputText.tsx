/* eslint-disable @typescript-eslint/no-explicit-any */
import { InputProps } from "@mui/material";
import { HTMLInputTypeAttribute } from "react";
import { Controller } from "react-hook-form";
import TextInput from "./TextInput";

type FormInputProps = {
  name: string;
  control: any;
  label: string;
  type: HTMLInputTypeAttribute;
  placeholder?: string;
  inputProps?: InputProps;
  multiline?: boolean;
  helperText?: string | null;
  disabled?: boolean;
};

export const FormInputText = ({
  name,
  control,
  label,
  type,
  placeholder,
  inputProps,
  helperText,
  ...rest
}: FormInputProps) => {
  return (
    <Controller
      name={name}
      control={control}
      render={({ field: { onChange, value }, fieldState: { error } }) => (
        <TextInput
          {...rest}
          helperText={error ? error.message : helperText ? helperText : null}
          error={!!error}
          onChange={
            type === "number" ? e => onChange(+e.target.value) : onChange
          }
          value={value}
          label={label}
          type={type}
          placeholder={placeholder}
          InputProps={inputProps}
        />
      )}
    />
  );
};
