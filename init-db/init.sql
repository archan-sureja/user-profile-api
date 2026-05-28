--
-- PostgreSQL database dump
--

\restrict H48L2UkcUKLkSaXfTq1Tk9pie1WnUrMQhBHKZTm5XivJQaNLgCA9myrhQaXFrir

-- Dumped from database version 18.2 (Ubuntu 18.2-1.pgdg22.04+1)
-- Dumped by pg_dump version 18.2 (Ubuntu 18.2-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    username character varying(30) NOT NULL,
    password character varying(255) NOT NULL,
    email character varying(100) NOT NULL,
    is_admin boolean NOT NULL,
    is_active boolean NOT NULL,
    bio text
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
7320fd217b0e
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, first_name, last_name, username, password, email, is_admin, is_active, bio) FROM stdin;
10	john	string	stringst	$argon2id$v=19$m=65536,t=3,p=4$SR0QrVJvCIvuSYFd1pd77g$xJUE6wII7yXdEEAr38fl7xqw9l7ILHF37ib8SVC+z4o	user@example.com	f	t	string
13	john	j	stringst1	$argon2id$v=19$m=65536,t=3,p=4$60RJRjnj37Uwg2+GGICnqg$z7/OYe4aLMKCR9BMlbbmeGRhfGzTPUfPz1CQiY5CNLs	user1@example.com	f	t	string
14	john	j	stringst11	$argon2id$v=19$m=65536,t=3,p=4$zsi83FPaiQXUIwYNKtxliw$OLctS3iZ1DqQMaOaV/Nk4/RP/Gb8YI1FLM5NcWr4n1Y	user11@example.com	f	t	   this is is included without leading and trailing spaces    
15	john	j	stringst14	$argon2id$v=19$m=65536,t=3,p=4$vg0+IMigWVdUZYpl1k2mnw$deZfqrHCjsrFZuMphpZD4C5upvESS5fiqwn0FekP2jY	user14@example.com	f	t	\N
16	john	doe	john.doe123	$argon2id$v=19$m=65536,t=3,p=4$S3BxdvTfve12lGXqpKHMzg$WStt+7eqrqt4FDcrNwmcodzqdA/Dn9dd8Uomx/NU0HM	john@example.com	f	t	this is test bio
17	john	doe	john.doe1234	$argon2id$v=19$m=65536,t=3,p=4$IVf7oSTzLkc5h/B5rJGsGg$UJBgzyI4ST8OXWX7xHC146PeJQAh8mXm99+GpD2n8lU	john1@example.com	f	t	this is test bio
18	john	doe	john.doe1231	$argon2id$v=19$m=65536,t=3,p=4$ccNAiXjCGmu5qJXbAGO4lA$5mW05SLK90wH7IkMSx0X6loo0DaSXKpznfnvkCwJ5GE	john0@example.com	t	t	this is test bio
20	john	doe	john.doe1111	$argon2id$v=19$m=65536,t=3,p=4$Yi/ruvnupgasmXJ2gQjnGQ$Hldzp5IBYR02xhpe/E3vEJ84LgVRfl8RJat6tte8/TI	john1111@example.com	f	t	this is test bio
22	test	doe	test.doe1111	$argon2id$v=19$m=65536,t=3,p=4$KLePYgyiTzhozhRXtavlsQ$p0JFxc54wodJtIi96nf5CDGm5WmtsijkvU81UwKXNDQ	test1111@example.com	f	t	this is test bio
23	testt	doe	test.doe111	$argon2id$v=19$m=65536,t=3,p=4$yd6hGL2fc+etmpMGXm2dLQ$fkXldFtK0zU8kqFK9+aGjIRYWBgfYf7jj9GSM09ktko	test111@example.com	f	t	this is test bio
25	admin	admin	admin.user123	$argon2id$v=19$m=65536,t=3,p=4$eISv5JM1xfKx09QGlcPaqQ$g5ZcNZ8BGJY5e43FU8rFQfSs599jdKpjP1CcvL5V3kA	admin.user@example.com	t	t	this is test bio
21	archan	sureja	archan_123	$argon2id$v=19$m=65536,t=3,p=4$8NctR6PtG95Ne9jSCBsSMg$DJHNUDx3Z9XQzfB6KinaJEHOXM5EiAaLYYPXM+QGOn4	archan@example.com	f	f	\N
24	bad	user	bad.user123	$argon2id$v=19$m=65536,t=3,p=4$4rG+AtovA4uek0RfT4NNmQ$PlrUaHefB78+ERnmL3A6AI/MVLA4fOD/sx/NM7GtB6o	bad.user@example.com	f	f	this is test bio
29	j	j	j.changed.user123	$argon2id$v=19$m=65536,t=3,p=4$cnkoPR/vbm3HqMn0yOKxdw$4hIVGTF0+Tc1B8hxXn2ygMwKNJFH/6m2DuoP/HqKaKo	j.user@example.com	f	t	\N
30	my	admin	my.admin	$argon2id$v=19$m=65536,t=3,p=4$exvEbCuXfdZvGshoIqGj5w$7wnp3yHc2kUtNDQ1B4aaP0ei8MmRpl5Ju/GraQd2SV0	myadmin@example.com	t	t	\N
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 30, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- PostgreSQL database dump complete
--

\unrestrict H48L2UkcUKLkSaXfTq1Tk9pie1WnUrMQhBHKZTm5XivJQaNLgCA9myrhQaXFrir

