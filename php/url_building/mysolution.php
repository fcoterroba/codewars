<?php

<?php
class URLBuilder
{
    private string $scheme;
    private ?string $user;
    private ?string $pass;
    private string $host;
    private string $port;
    private ?string $path;
    private array $query;
    private ?string $fragment;

    public function __construct(array $params)
    {
        if (empty($params['host'])) {
            throw new InvalidArgumentException("'host' is required.");
        }
        if (isset($params['query']) && !is_array($params['query'])) {
            throw new InvalidArgumentException("'query' must be an array.");
        }

        $this->scheme   = !empty($params['scheme']) ? $params['scheme'] : 'http';
        $this->user     = isset($params['user']) && $params['user'] !== '' ? $params['user'] : null;
        $this->pass     = isset($params['pass']) && $params['pass'] !== '' ? $params['pass'] : null;
        $this->host     = $params['host'];
        $this->port     = !empty($params['port']) ? $params['port'] : '80';
        $this->query    = !empty($params['query']) ? $params['query'] : [];
        $this->fragment = !empty($params['fragment']) ? $params['fragment'] : null;

        if (!array_key_exists('path', $params)) {
            $this->path = '/';
        } elseif ($params['path'] === '' || $params['path'] === null) {
            $this->path = null;
        } else {
            $this->path = $params['path'];
        }
    }

    public function build(): string
    {
        $url = $this->scheme . '://';

        if ($this->user !== null && $this->pass !== null) {
            $url .= rawurlencode($this->user) . ':' . rawurlencode($this->pass) . '@';
        }

        $url .= $this->host;

        if ($this->port !== '80') {
            $url .= ':' . $this->port;
        }

        if ($this->path !== null) {
            $url .= $this->path;
        }

        if (!empty($this->query)) {
            $url .= '?' . http_build_query($this->query);
        }

        if ($this->fragment !== null) {
            $url .= '#' . $this->fragment;
        }

        return $url;
    }
}

// original kata: https://www.codewars.com/kata/585de868851516395e0003d3
// my solution: https://www.codewars.com/kata/reviews/585de8751cfd06401500006c/groups/69fc464cf743306e771bba48
